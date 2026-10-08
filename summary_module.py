from gemini_service import generate_text

def summarize_text(text: str) -> str:
    prompt = f"""
Summarize the following educational text for a student.

Requirements:
- Preserve the important facts and meaning.
- Remove repetition.
- Use clear, simple language.
- Prefer a short paragraph followed by 3-6 key points.
- Do not add facts that are not present in the text.

Text:
{text}
"""
    return generate_text(prompt)
