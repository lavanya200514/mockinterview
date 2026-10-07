"use strict";

const TOTAL_QUESTIONS = 10;
const interviewError = document.querySelector("#interview-error");
let interview;
let currentQuestion = 0;
let answers = Array(TOTAL_QUESTIONS).fill(null);

try {
  interview = JSON.parse(sessionStorage.getItem("mockmateInterview") || "null");
} catch {
  interview = null;
}

if (!interview || !interview.interview_id || !Array.isArray(interview.questions) || interview.questions.length !== TOTAL_QUESTIONS) {
  window.location.replace("/");
} else {
  document.querySelector("#interview-subject").textContent = `${interview.subject} / ${interview.difficulty}`;
  document.querySelector("#student-greeting").textContent = `Ready, ${interview.student_name}?`;
  renderQuestion();
}

document.querySelector("#previous-button").addEventListener("click", () => {
  if (currentQuestion > 0) {
    currentQuestion -= 1;
    renderQuestion();
  }
});

document.querySelector("#next-button").addEventListener("click", () => {
  if (currentQuestion < TOTAL_QUESTIONS - 1) {
    currentQuestion += 1;
    renderQuestion();
  }
});

document.querySelector("#submit-button").addEventListener("click", async () => {
  const firstUnanswered = answers.findIndex((answer) => answer === null);
  if (firstUnanswered !== -1) {
    interviewError.textContent = `Please answer question ${firstUnanswered + 1} before submitting.`;
    interviewError.hidden = false;
    currentQuestion = firstUnanswered;
    renderQuestion();
    return;
  }
  if (!window.confirm("Are you sure you want to submit your interview?")) return;

  const submitButton = document.querySelector("#submit-button");
  submitButton.disabled = true;
  submitButton.textContent = "Evaluating answers...";
  interviewError.hidden = true;
  try {
    const response = await fetch("/api/evaluate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ interview_id: interview.interview_id, answers }),
    });
    const result = await response.json();
    if (!response.ok) throw new Error(result.error || "Your answers could not be evaluated.");
    sessionStorage.setItem("mockmateResult", JSON.stringify({ interview_id: interview.interview_id, result }));
    window.location.assign("/result");
  } catch (error) {
    interviewError.textContent = error instanceof TypeError
      ? "We could not reach the server. Check your connection and try submitting again."
      : error.message;
    interviewError.hidden = false;
    submitButton.disabled = false;
    submitButton.innerHTML = "Submit interview <span aria-hidden='true'>↗</span>";
  }
});

function renderQuestion() {
  const question = interview.questions[currentQuestion];
  const number = currentQuestion + 1;
  document.querySelector("#question-count").textContent = `Question ${number} of ${TOTAL_QUESTIONS}`;
  document.querySelector("#question-number").textContent = String(number).padStart(2, "0");
  document.querySelector("#question-text").textContent = question.question;
  document.querySelector("#question-level").textContent = `QUESTION ${String(number).padStart(2, "0")}`;
  const answered = answers.filter((answer) => answer !== null).length;
  document.querySelector("#answered-count").textContent = `${answered} answered`;
  document.querySelector("#progress-fill").style.width = `${(number / TOTAL_QUESTIONS) * 100}%`;
  document.querySelector(".progress-track").setAttribute("aria-valuenow", String(answered));
  document.querySelector("#previous-button").disabled = currentQuestion === 0;
  document.querySelector("#next-button").hidden = currentQuestion === TOTAL_QUESTIONS - 1;
  document.querySelector("#submit-button").hidden = currentQuestion !== TOTAL_QUESTIONS - 1;

  const options = document.querySelector("#answer-options");
  options.replaceChildren();
  for (const letter of ["A", "B", "C", "D"]) {
    const label = document.createElement("label");
    label.className = "answer-option";
    if (answers[currentQuestion] === letter) label.classList.add("is-selected");
    const input = document.createElement("input");
    input.type = "radio";
    input.name = "answer";
    input.value = letter;
    input.checked = answers[currentQuestion] === letter;
    input.addEventListener("change", () => {
      answers[currentQuestion] = letter;
      renderQuestion();
    });
    const marker = document.createElement("span");
    marker.className = "option-letter";
    marker.textContent = letter;
    const text = document.createElement("span");
    text.className = "option-copy";
    text.textContent = question.options[letter];
    label.append(input, marker, text);
    options.append(label);
  }
}