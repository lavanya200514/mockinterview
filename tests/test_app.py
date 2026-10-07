from __future__ import annotations

import pytest

import app as app_module
from services import ai_service


@pytest.fixture
def client():
    app_module._interviews.clear()
    application = app_module.create_app({"TESTING": True})
    return application.test_client()


def start_interview(client, subject="Python", difficulty="Intermediate"):
    return client.post("/api/generate-questions", json={
        "student_name": "Taylor",
        "subject": subject,
        "difficulty": difficulty,
    })


@pytest.mark.parametrize("subject", ai_service.QUESTION_BANK)
@pytest.mark.parametrize("difficulty", ("Beginner", "Intermediate", "Expert"))
def test_each_subject_and_level_has_a_valid_randomized_question_set(client, subject, difficulty):
    bank = ai_service.QUESTION_BANK[subject][difficulty]
    assert len(bank) >= 10
    assert all(len(question["options"]) == 4 and question["answer"] in question["options"] for question in bank)

    questions = ai_service.generate_interview(subject, difficulty)
    assert len(questions) == 10
    assert len({question["question"] for question in questions}) == 10
    assert all(set(question["options"]) == {"A", "B", "C", "D"} for question in questions)
    assert all(question["correct_answer"] in {"A", "B", "C", "D"} for question in questions)
    assert all(question["explanation"] for question in questions)


def test_generation_validates_fields(client):
    invalid_requests = [
        {"student_name": "", "subject": "Python", "difficulty": "Beginner"},
        {"student_name": "Taylor", "subject": "Unknown", "difficulty": "Beginner"},
        {"student_name": "Taylor", "subject": "Python", "difficulty": "Advanced"},
        {"student_name": "Taylor", "subject": [], "difficulty": "Beginner"},
    ]
    for payload in invalid_requests:
        response = client.post("/api/generate-questions", json=payload)
        assert response.status_code == 400
        assert "error" in response.json


def test_generation_works_without_an_openai_api_key(client, monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    response = start_interview(client, "Python", "Beginner")
    assert response.status_code == 201
    assert len(response.json["questions"]) == 10
    assert "OpenAI" not in response.get_data(as_text=True)


def test_generated_questions_hide_answers_and_preserve_the_session(client):
    response = start_interview(client)
    assert response.status_code == 201
    assert len(response.json["questions"]) == 10
    assert "correct_answer" not in response.json["questions"][0]
    assert "explanation" not in response.json["questions"][0]
    assert response.json["interview_id"] in app_module._interviews


def test_evaluation_requires_all_answers_and_returns_a_scored_pdf(client):
    started = start_interview(client)
    interview_id = started.json["interview_id"]
    questions = app_module._interviews[interview_id]["questions"]
    answers = [
        question["correct_answer"] if index < 5 else next(
            letter for letter in "ABCD" if letter != question["correct_answer"]
        )
        for index, question in enumerate(questions)
    ]

    missing = client.post("/api/evaluate", json={
        "interview_id": interview_id,
        "answers": [None] + answers[1:],
    })
    assert missing.status_code == 400
    assert "answer question 1" in missing.json["error"]

    response = client.post("/api/evaluate", json={"interview_id": interview_id, "answers": answers})
    assert response.status_code == 200
    assert response.json["total_questions"] == 10
    assert response.json["correct_answers"] == 5
    assert response.json["wrong_answers"] == 5
    assert response.json["score"] == "5/10"
    assert response.json["percentage"] == 50
    assert response.json["review"][0]["status"] == "correct"
    assert response.json["review"][5]["status"] == "wrong"
    assert response.json["review"][0]["explanation"]

    pdf_response = client.post("/api/download-pdf", json={"interview_id": interview_id})
    assert pdf_response.status_code == 200
    assert pdf_response.mimetype == "application/pdf"
    assert pdf_response.data.startswith(b"%PDF")


def test_invalid_or_missing_interview_is_rejected(client):
    missing_id = client.post("/api/evaluate", json={"answers": ["A"] * 10})
    assert missing_id.status_code == 400

    unknown_id = client.post("/api/evaluate", json={"interview_id": "missing", "answers": ["A"] * 10})
    assert unknown_id.status_code == 404


def test_wrong_answer_count_is_rejected(client):
    started = start_interview(client)
    response = client.post("/api/evaluate", json={
        "interview_id": started.json["interview_id"],
        "answers": ["A"] * 9,
    })
    assert response.status_code == 400
    assert "all 10 questions" in response.json["error"]