"""Flask application for local mock interviews."""

from __future__ import annotations

import os
import threading
import time
import uuid
from datetime import datetime, timezone
from typing import Any

from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request, send_file

from services import ai_service, pdf_service

load_dotenv()

SUBJECTS = {"Full Stack Development", "Java", "Python", "Cyber Security"}
DIFFICULTIES = {"Beginner", "Intermediate", "Expert"}
INTERVIEW_TTL_SECONDS = 60 * 60 * 4
_interviews: dict[str, dict[str, Any]] = {}
_interviews_lock = threading.Lock()


def create_app(test_config: dict[str, Any] | None = None) -> Flask:
    app = Flask(__name__)
    app.config.from_mapping(MAX_CONTENT_LENGTH=32 * 1024, JSON_SORT_KEYS=False)
    if test_config:
        app.config.update(test_config)

    @app.after_request
    def set_security_headers(response):
        response.headers.setdefault("X-Content-Type-Options", "nosniff")
        response.headers.setdefault("X-Frame-Options", "DENY")
        response.headers.setdefault("Referrer-Policy", "strict-origin-when-cross-origin")
        response.headers.setdefault("Content-Security-Policy", "default-src 'self'; style-src 'self' https://fonts.googleapis.com; script-src 'self'; img-src 'self' data:; font-src 'self' https://fonts.gstatic.com; connect-src 'self'; object-src 'none'; base-uri 'self'; frame-ancestors 'none'")
        return response

    @app.get("/")
    def home():
        return render_template("index.html")

    @app.get("/interview")
    def interview_page():
        return render_template("interview.html")

    @app.get("/result")
    def result_page():
        return render_template("result.html")

    @app.post("/api/generate-questions")
    def generate_questions():
        payload = request.get_json(silent=True)
        if not isinstance(payload, dict):
            return _error("Please submit valid interview details.", 400)

        name = payload.get("student_name")
        subject = payload.get("subject")
        difficulty = payload.get("difficulty")
        if not isinstance(name, str) or not name.strip() or len(name.strip()) > 80:
            return _error("Enter your name (up to 80 characters) to continue.", 400)
        if not isinstance(subject, str) or subject not in SUBJECTS:
            return _error("Choose one of the supported interview subjects.", 400)
        if not isinstance(difficulty, str) or difficulty not in DIFFICULTIES:
            return _error("Choose a valid difficulty level.", 400)

        questions = ai_service.generate_interview(subject, difficulty)

        interview_id = uuid.uuid4().hex
        record = {
            "student_name": name.strip(),
            "subject": subject,
            "difficulty": difficulty,
            "questions": questions,
            "created_at": datetime.now(timezone.utc).isoformat(),
            "created_monotonic": time.monotonic(),
            "result": None,
        }
        with _interviews_lock:
            _purge_expired_interviews()
            _interviews[interview_id] = record

        return jsonify({
            "interview_id": interview_id,
            "student_name": record["student_name"],
            "subject": subject,
            "difficulty": difficulty,
            "questions": [ai_service.public_question(question) for question in questions],
        }), 201

    @app.post("/api/evaluate")
    def evaluate():
        payload = request.get_json(silent=True)
        if not isinstance(payload, dict):
            return _error("Please submit a valid answer sheet.", 400)
        interview_id = payload.get("interview_id")
        answers = payload.get("answers")
        if not isinstance(interview_id, str) or not interview_id.strip():
            return _error("The interview ID is missing or invalid. Please start a new interview.", 400)
        if not isinstance(answers, list) or len(answers) != 10:
            return _error("Please submit answers for all 10 questions.", 400)

        with _interviews_lock:
            record = _get_interview(interview_id)
            if record is None:
                return _error("This interview could not be found or has expired. Start a new one to continue.", 404)
            if record["result"] is not None:
                return jsonify(record["result"])
            try:
                result = _evaluate_answers(record, answers)
            except ValueError as error:
                return _error(str(error), 400)
            record["result"] = result
        return jsonify(result)

    @app.post("/api/download-pdf")
    def download_pdf():
        payload = request.get_json(silent=True)
        interview_id = payload.get("interview_id") if isinstance(payload, dict) else None
        if not isinstance(interview_id, str):
            return _error("The report could not be found. Submit an interview first.", 400)
        with _interviews_lock:
            record = _get_interview(interview_id)
            if record is None or record["result"] is None:
                return _error("Submit a valid interview before downloading its report.", 404)
            report = record["result"]
        try:
            pdf = pdf_service.build_report(report)
        except Exception:
            app.logger.exception("PDF report generation failed")
            return _error("Your PDF report could not be created. Please try again.", 500)
        filename = f"mock-interview-{interview_id[:8]}.pdf"
        return send_file(pdf, mimetype="application/pdf", as_attachment=True, download_name=filename)

    return app


def _error(message: str, status: int):
    return jsonify({"error": message}), status


def _purge_expired_interviews() -> None:
    now = time.monotonic()
    expired = [key for key, value in _interviews.items() if now - value["created_monotonic"] > INTERVIEW_TTL_SECONDS]
    for key in expired:
        del _interviews[key]


def _get_interview(interview_id: str) -> dict[str, Any] | None:
    _purge_expired_interviews()
    return _interviews.get(interview_id)


def _evaluate_answers(record: dict[str, Any], answers: list[Any]) -> dict[str, Any]:
    result = ai_service.evaluate_interview(record["questions"], answers)
    result.update({
        "student_name": record["student_name"],
        "subject": record["subject"],
        "difficulty": record["difficulty"],
        "date": datetime.now(timezone.utc).strftime("%B %d, %Y"),
        "performance_message": _performance_message(result["percentage"]),
        "recommendation": _recommendation(result["percentage"], record["subject"]),
    })
    return result


def _performance_message(percentage: float) -> str:
    if percentage >= 90:
        return "Excellent! You have demonstrated strong knowledge."
    if percentage >= 75:
        return "Very Good! You have a good understanding of the subject."
    if percentage >= 60:
        return "Good! Keep practicing to improve your technical skills."
    if percentage >= 40:
        return "Needs Improvement. Review the important concepts and practice more."
    return "Beginner Level. We recommend revising the fundamentals and attempting another mock interview."


def _recommendation(percentage: float, subject: str) -> str:
    if percentage >= 90:
        return f"Maintain your momentum with advanced {subject} problems and explain your reasoning aloud."
    if percentage >= 75:
        return f"Strengthen a few gaps by revisiting the questions you missed, then try an Expert {subject} interview."
    if percentage >= 60:
        return f"Review the core {subject} concepts behind missed answers and practice applying them in small exercises."
    return f"Revisit the {subject} fundamentals, study each explanation in this report, and retake the interview after practice."


app = create_app()


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=int(os.getenv("PORT", "5001")), debug=os.getenv("FLASK_DEBUG") == "1")