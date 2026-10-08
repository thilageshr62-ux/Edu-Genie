from gemini_service import generate_text

def get_learning_recommendations(topic: str, level: str = "Beginner") -> str:
    prompt = f"""
Create a personalized learning path for the topic: {topic}
Learner level: {level}

Organize it from beginner to advanced. Include:
1. Prerequisites
2. Ordered topics/modules
3. Suggested timeline
4. Practice activities or mini-projects
5. Recommended resource types (videos, articles, books, documentation)
6. A simple checkpoint for measuring progress

Keep it practical and student-friendly. Do not invent specific URLs.
"""
    return generate_text(prompt)
