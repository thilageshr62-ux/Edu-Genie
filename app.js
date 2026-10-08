const task = document.getElementById("task");
const input = document.getElementById("inputText");
const label = document.getElementById("input-label");
const level = document.getElementById("level");
const levelLabel = document.getElementById("level-label");
const button = document.getElementById("submitBtn");
const result = document.getElementById("result");
const status = document.getElementById("status");
const copyBtn = document.getElementById("copyBtn");

const configs = {
    qa: {
        label: "Question",
        placeholder: "Example: Which is the largest ocean?"
    },
    explain: {
        label: "Topic",
        placeholder: "Example: Explain the Pythagoras theorem for a beginner."
    },
    quiz: {
        label: "Passage",
        placeholder: "Paste at least a short educational passage here..."
    },
    summarize: {
        label: "Text to summarize",
        placeholder: "Paste the educational passage you want to summarize..."
    },
    learn: {
        label: "Topic",
        placeholder: "Example: SQL"
    }
};

task.addEventListener("change", updateForm);
copyBtn.addEventListener("click", copyResult);
button.addEventListener("click", submitTask);

function updateForm() {
    const cfg = configs[task.value];
    label.textContent = cfg.label;
    input.placeholder = cfg.placeholder;
    const showLevel = task.value === "learn";
    level.classList.toggle("hidden", !showLevel);
    levelLabel.classList.toggle("hidden", !showLevel);
}

async function submitTask() {
    const text = input.value.trim();
    if (!text) {
        setStatus("Please enter something first.");
        return;
    }

    button.disabled = true;
    setStatus("EduGenie is thinking...");
    result.className = "result empty";
    result.textContent = "Generating...";

    const endpointMap = {
        qa: "/qa",
        explain: "/explain",
        quiz: "/quiz",
        summarize: "/summarize",
        learn: "/learn/recommendations"
    };

    const bodyMap = {
        qa: { question: text },
        explain: { topic: text },
        quiz: { text },
        summarize: { text },
        learn: { topic: text, level: level.value }
    };

    try {
        const response = await fetch(endpointMap[task.value], {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(bodyMap[task.value])
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.detail || "Request failed.");
        }

        result.className = "result";
        if (task.value === "quiz") {
            renderQuiz(data.result);
        } else {
            result.textContent = data.result;
        }
        setStatus("Completed.");
    } catch (error) {
        result.className = "result";
        result.textContent = "Error: " + error.message;
        setStatus("Something went wrong.");
    } finally {
        button.disabled = false;
    }
}

function renderQuiz(questions) {
    result.innerHTML = "";
    questions.forEach((q, index) => {
        const wrapper = document.createElement("div");
        wrapper.className = "quiz-question";

        const title = document.createElement("h3");
        title.textContent = `${index + 1}. ${q.question}`;
        wrapper.appendChild(title);

        q.options.forEach(option => {
            const optionLabel = document.createElement("label");
            optionLabel.className = "quiz-option";

            const radio = document.createElement("input");
            radio.type = "radio";
            radio.name = `quiz-${index}`;
            radio.value = option;

            radio.addEventListener("change", () => {
                const feedback = wrapper.querySelector(".quiz-feedback");
                if (option === q.answer) {
                    feedback.textContent = "Correct! " + (q.explanation || "");
                } else {
                    feedback.textContent = `Not quite. Correct answer: ${q.answer}. ${q.explanation || ""}`;
                }
            });

            optionLabel.appendChild(radio);
            optionLabel.appendChild(document.createTextNode(" " + option));
            wrapper.appendChild(optionLabel);
        });

        const feedback = document.createElement("div");
        feedback.className = "quiz-feedback";
        wrapper.appendChild(feedback);
        result.appendChild(wrapper);
    });
}

function setStatus(message) {
    status.textContent = message;
}

async function copyResult() {
    const text = result.innerText.trim();
    if (!text) return;
    await navigator.clipboard.writeText(text);
    setStatus("Result copied.");
}

updateForm();
