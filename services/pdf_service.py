"""Create a downloadable, readable PDF interview report."""

from __future__ import annotations

from io import BytesIO
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


def build_report(report: dict) -> BytesIO:
    output = BytesIO()
    document = SimpleDocTemplate(
        output,
        pagesize=letter,
        rightMargin=0.7 * inch,
        leftMargin=0.7 * inch,
        topMargin=0.65 * inch,
        bottomMargin=0.65 * inch,
        title="AI Mock Interview Report",
        author="AI Mock Interview System",
    )
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name="ReportTitle", parent=styles["Title"], fontName="Helvetica-Bold", fontSize=20, leading=24, textColor=colors.HexColor("#152c2b"), alignment=TA_LEFT, spaceAfter=8))
    styles.add(ParagraphStyle(name="QuestionHeading", parent=styles["Heading3"], fontName="Helvetica-Bold", fontSize=10, leading=13, textColor=colors.HexColor("#176b60"), spaceBefore=12, spaceAfter=4))
    styles.add(ParagraphStyle(name="ReportBody", parent=styles["BodyText"], fontSize=9, leading=13, spaceAfter=4))
    styles.add(ParagraphStyle(name="SmallLabel", parent=styles["BodyText"], fontSize=8, leading=11, textColor=colors.HexColor("#50615f")))

    story = [Paragraph("AI MOCK INTERVIEW REPORT", styles["ReportTitle"])]
    story.append(Paragraph(
        f"<b>Student:</b> {_safe(report.get('student_name'))} &nbsp;&nbsp; "
        f"<b>Subject:</b> {_safe(report.get('subject'))} &nbsp;&nbsp; "
        f"<b>Difficulty:</b> {_safe(report.get('difficulty'))}<br/>"
        f"<b>Date:</b> {_safe(report.get('date'))}",
        styles["ReportBody"],
    ))
    story.append(Spacer(1, 10))
    story.append(Paragraph("PERFORMANCE SUMMARY", styles["Heading2"]))
    summary = [
        ["Total Questions", "Correct", "Wrong", "Unanswered", "Score", "Percentage"],
        [str(report["total_questions"]), str(report["correct_answers"]), str(report["wrong_answers"]), str(report["unanswered"]), str(report["score"]), f"{report['percentage']}%"],
    ]
    table = Table(summary, colWidths=[1.04 * inch] * 6, repeatRows=1)
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#e9f2ef")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.HexColor("#152c2b")),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
        ("FONTSIZE", (0, 0), (-1, -1), 8),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#ccd8d4")),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
    ]))
    story.extend([table, Spacer(1, 10), Paragraph(_safe(report["performance_message"]), styles["ReportBody"]), Paragraph("ANSWER REVIEW", styles["Heading2"])])

    for item in report["review"]:
        selected = item["your_answer"]
        your_answer = f"{selected}. {item['options'][selected]}" if selected else "Not answered"
        correct = item["correct_answer"]
        correct_answer = f"{correct}. {item['options'][correct]}"
        status = {"correct": "Correct", "wrong": "Wrong", "unanswered": "Not Answered"}[item["status"]]
        story.extend([
            Paragraph(f"Question {item['number']}", styles["QuestionHeading"]),
            Paragraph(_safe(item["question"]), styles["ReportBody"]),
            Paragraph(f"<b>Your answer:</b> {_safe(your_answer)}<br/><b>Correct answer:</b> {_safe(correct_answer)}<br/><b>Result:</b> {_safe(status)}", styles["ReportBody"]),
            Paragraph(f"<b>Explanation:</b> {_safe(item['explanation'])}", styles["ReportBody"]),
        ])

    story.extend([Spacer(1, 10), Paragraph("RECOMMENDATIONS", styles["Heading2"]), Paragraph(_safe(report["recommendation"]), styles["ReportBody"])])
    document.build(story)
    output.seek(0)
    return output


def _safe(value: object) -> str:
    return escape(str(value))