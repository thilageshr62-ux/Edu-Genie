from gemini_service import generate_text

def explain_concept(topic: str) -> str:
    prompt = f"""
You are EduGenie explaining a concept to a beginner.

Concept: {topic}

Create an easy-to-understand explanation with:
1. A one-sentence definition
2. Main idea in simple language
3. A small real-world or academic example
4. Key points to remember

Avoid unnecessary jargon. Keep the response concise.
"""
    return generate_text(prompt)
