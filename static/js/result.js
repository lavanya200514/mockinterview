"use strict";

const resultError = document.querySelector("#result-error");
let saved;
try {
  saved = JSON.parse(sessionStorage.getItem("mockmateResult") || "null");
} catch {
  saved = null;
}

if (!saved?.result || !saved?.interview_id) {
  window.location.replace("/");
} else {
  renderResult(saved.result);
}

document.querySelector("#download-pdf").addEventListener("click", async (event) => {
  const button = event.currentTarget;
  button.disabled = true;
  resultError.hidden = true;
  try {
    const response = await fetch("/api/download-pdf", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ interview_id: saved.interview_id }),
    });
    if (!response.ok) {
      const data = await response.json();
      throw new Error(data.error || "The PDF could not be downloaded.");
    }
    const blob = await response.blob();
    const downloadUrl = URL.createObjectURL(blob);
    const link = document.createElement("a");
    link.href = downloadUrl;
    link.download = "ai-mock-interview-report.pdf";
    link.click();
    URL.revokeObjectURL(downloadUrl);
  } catch (error) {
    resultError.textContent = error instanceof TypeError
      ? "We could not reach the server. Check your connection and try again."
      : error.message;
    resultError.hidden = false;
  } finally {
    button.disabled = false;
  }
});

function renderResult(result) {
  document.querySelector("#result-title").innerHTML = `Well done, ${escapeHtml(result.student_name)}.<br><span>Here’s your breakdown.</span>`;
  document.querySelector("#performance-message").textContent = result.performance_message;
  document.querySelector("#score-percentage").textContent = `${result.percentage}%`;
  document.querySelector("#score-fraction").textContent = result.score;
  document.querySelector("#total-questions").textContent = result.total_questions;
  document.querySelector("#correct-answers").textContent = result.correct_answers;
  document.querySelector("#wrong-answers").textContent = result.wrong_answers;
  document.querySelector("#unanswered-count").textContent = result.unanswered;
  document.querySelector("#recommendation-text").textContent = result.recommendation;
  document.querySelector("#report-date").textContent = result.date;
  const reviewList = document.querySelector("#review-list");
  for (const item of result.review) {
    const article = document.createElement("article");
    article.className = `review-item review-${item.status}`;
    const heading = document.createElement("div");
    heading.className = "review-heading";
    const questionNumber = document.createElement("span");
    questionNumber.className = "review-number";
    questionNumber.textContent = `Q${String(item.number).padStart(2, "0")}`;
    const status = document.createElement("span");
    status.className = "review-status";
    status.textContent = { correct: "✓ Correct", wrong: "× Wrong", unanswered: "○ Not answered" }[item.status];
    heading.append(questionNumber, status);
    const question = document.createElement("h3");
    question.textContent = item.question;
    const answers = document.createElement("div");
    answers.className = "review-answers";
    const userAnswer = item.your_answer ? `${item.your_answer}. ${item.options[item.your_answer]}` : "Not answered";
    const correctAnswer = `${item.correct_answer}. ${item.options[item.correct_answer]}`;
    answers.append(makeAnswerBlock("YOUR ANSWER", userAnswer), makeAnswerBlock("CORRECT ANSWER", correctAnswer));
    const explanation = document.createElement("p");
    explanation.className = "review-explanation";
    explanation.textContent = item.explanation;
    article.append(heading, question, answers, explanation);
    reviewList.append(article);
  }
}

function makeAnswerBlock(label, value) {
  const block = document.createElement("div");
  const heading = document.createElement("span");
  heading.textContent = label;
  const answer = document.createElement("p");
  answer.textContent = value;
  block.append(heading, answer);
  return block;
}

function escapeHtml(value) {
  const span = document.createElement("span");
  span.textContent = value;
  return span.innerHTML;
}