"use strict";

const setupForm = document.querySelector("#setup-form");
const setupError = document.querySelector("#setup-error");
const submitButton = setupForm.querySelector("button[type='submit']");

setupForm.addEventListener("submit", async (event) => {
  event.preventDefault();
  setupError.hidden = true;
  const studentName = setupForm.elements.student_name.value.trim();
  const subject = setupForm.elements.subject.value;
  const difficulty = setupForm.elements.difficulty.value;

  if (!studentName || !subject || !difficulty) {
    setupError.textContent = "Please enter your name and choose a subject and difficulty.";
    setupError.hidden = false;
    return;
  }

  submitButton.disabled = true;
  submitButton.innerHTML = "<span>Creating your questions...</span><span aria-hidden='true'>◌</span>";
  try {
    const response = await fetch("/api/generate-questions", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ student_name: studentName, subject, difficulty }),
    });
    const data = await response.json();
    if (!response.ok) throw new Error(data.error || "We could not start your interview.");
    sessionStorage.setItem("mockmateInterview", JSON.stringify(data));
    sessionStorage.removeItem("mockmateResult");
    window.location.assign("/interview");
  } catch (error) {
    setupError.textContent = error instanceof TypeError
      ? "We could not reach the server. Check your connection and try again."
      : error.message;
    setupError.hidden = false;
  } finally {
    submitButton.disabled = false;
    submitButton.innerHTML = "<span>Generate my interview</span><span aria-hidden='true'>↗</span>";
  }
});