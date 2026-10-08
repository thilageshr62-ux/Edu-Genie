from gemini_service import generate_json

def generate_quiz(text: str) -> list[dict]:
    prompt = f"""
Create exactly 3 multiple-choice questions from the educational passage below.

Return ONLY valid JSON as an array. Do not use Markdown.
Each object must have:
- "question": string
- "options": array of exactly 4 strings
- "answer": string containing exactly one of the option strings
- "explanation": short string explaining the correct answer

Passage:
{text}
"""
    data = generate_json(prompt)

    if not isinstance(data, list) or len(data) != 3:
        raise RuntimeError("Quiz generation did not return exactly 3 questions.")

    normalized = []
    for item in data:
        if not isinstance(item, dict):
            raise RuntimeError("Invalid quiz question format.")
        question = str(item.get("question", "")).strip()
        options = item.get("options", [])
        answer = str(item.get("answer", "")).strip()
        explanation = str(item.get("explanation", "")).strip()

        if not question or not isinstance(options, list) or len(options) != 4:
            raise RuntimeError("Each quiz question must contain four options.")
        options = [str(x).strip() for x in options]
        if answer not in options:
            raise RuntimeError("Quiz answer must match one of the options.")

        normalized.append({
            "question": question,
            "options": options,
            "answer": answer,
            "explanation": explanation,
        })
    return normalized
