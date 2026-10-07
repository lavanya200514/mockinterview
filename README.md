# AI Mock Interview

AI Mock Interview is a Flask-based technical interview practice application. Candidates choose a subject and level, answer a randomized set of multiple-choice questions, review their results and explanations, and download a PDF report. Questions come from a built-in Python bank; no API key or external AI service is required.

## Features

- 10 unique multiple-choice questions per interview, randomly selected from the local bank
- Four answer options per question; answers are checked on the server
- Score, percentage, correct answers, wrong answers, and final result
- Question-by-question review with selected answer, correct answer, and explanation
- Downloadable PDF report
- Session IDs, answer retention, question navigation, and progress indicator
- 12 built-in questions for every subject and level combination

## Subjects

- Full Stack Development
- Java
- Python
- Cyber Security

## Levels

- Beginner
- Intermediate
- Expert

Each interview contains exactly 10 questions selected without repetition from the chosen subject and level. Option order is shuffled for each interview.

## Technology Stack

- Python 3.10 or newer and Flask
- HTML, CSS, and vanilla JavaScript
- ReportLab for PDF generation
- pytest for automated tests

No OpenAI API key, paid API, or external AI service is used.

## Project Structure

```text
ai-mock-interview/
├── app.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
├── services/
│   ├── __init__.py
│   ├── ai_service.py
│   └── pdf_service.py
├── static/
│   ├── css/style.css
│   └── js/
│       ├── main.js
│       ├── interview.js
│       └── result.js
├── templates/
│   ├── index.html
│   ├── interview.html
│   └── result.html
├── tests/test_app.py
└── reports/
```

`reports/` is available for reports you may choose to archive; generated PDFs are streamed directly to the browser by default.

## Requirements

- Python 3.10 or newer
- No API key or external AI service is required

## Installation

Open a terminal in the `ai-mock-interview` directory and create a virtual environment:

```powershell
python -m venv venv
venv\Scripts\activate
python -m pip install -r requirements.txt
```

On macOS or Linux, activate it with `source venv/bin/activate`.

## Environment Setup

No API key is required. The optional `PORT` setting defaults to `5001`.

## How to Run

```powershell
python app.py runserver
```

Open <http://127.0.0.1:5001> in your browser. Keep the terminal open while using the app; press `Ctrl+C` to stop the development server. Do not use the development server for public production deployment; use a production WSGI server and HTTPS.

## How to Use

1. Enter a candidate name, choose one of the four subjects, and select a level.
2. Click **Generate my interview** and answer all 10 questions. Previous/Next navigation retains your choices.
3. Submit the interview to see the score, percentage, correct and wrong counts, and final result.
4. Review every selected answer, correct answer, and explanation, then download the PDF report.

## API Configuration and Routes

The backend loads `.env` with python-dotenv for optional local settings. Questions and scoring are handled entirely in Python without external API calls.

- `GET /`, `GET /interview`, `GET /result`: serve the application pages
- `POST /api/generate-questions`: accepts `student_name`, `subject`, and `difficulty`; returns an `interview_id` and ten public questions
- `POST /api/evaluate`: accepts `interview_id` and ten answer letters (`A`-`D` or `null`); returns the authoritative score and review
- `POST /api/download-pdf`: accepts `interview_id`; returns a PDF after evaluation

Example question-generation request:

```json
{
  "student_name": "Asha",
  "subject": "Python",
  "difficulty": "Beginner"
}
```

Example response shape (question wording and options are selected from the local bank):

```json
{
  "interview_id": "<opaque-session-id>",
  "student_name": "Asha",
  "subject": "Python",
  "difficulty": "Beginner",
  "questions": [
    {
      "question": "<generated question>",
      "options": {"A": "<option>", "B": "<option>", "C": "<option>", "D": "<option>"}
    }
  ]
}
```

The actual response contains exactly ten questions. Correct answers and explanations remain server-side until evaluation.

## Local Question Bank

The Python service stores 12 questions for each of the four subjects and three levels. It randomly samples ten distinct questions and shuffles their options for each interview. Correct answers remain on the server until submission.

For a multi-worker production deployment, replace the process-local interview store in `app.py` with a shared TTL-backed store such as Redis. The current in-memory store expires interview records after four hours and is suited to local/single-process use.

## PDF Generation

After evaluation, the backend passes its stored result to `services/pdf_service.py`. ReportLab lays out the summary table, each question's selected/correct answer and explanation, plus a recommendation. The PDF is streamed as an attachment; no client score or answer key is trusted for report generation.

## Testing

With the virtual environment active and dependencies installed:

```powershell
python -m pytest -q
```

Tests cover all subject/level question banks, generation without an API key, private answer keys, required answers, backend scoring, invalid sessions, and PDF downloads.

## Future Enhancements

- Shared persistent session storage for multi-worker deployments
- User accounts, saved history, and interview analytics
- Additional question formats and timed practice modes
- Accessibility/usability testing with a broader range of assistive technologies