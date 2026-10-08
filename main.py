from pathlib import Path

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from schemas import (
    ExplainRequest, LearningPathRequest, QARequest, QuizRequest, SummaryRequest
)
from qna import answer_question
from explanation_module import explain_concept
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import get_learning_recommendations

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(
    title="EduGenie - Google Gemini Powered Learning Assistant",
    version="1.0.0",
    description="Educational assistant with Q&A, explanations, quizzes, summaries and learning paths."
)

app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
   return templates.TemplateResponse(
    request=request,
    name="index.html",
    context={}
) 
@app.get("/health")
async def health():
    return {"status": "ok", "service": "EduGenie"}


@app.post("/qa")
async def qa(payload: QARequest):
    try:
        return {"success": True, "result": answer_question(payload.question)}
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))


@app.post("/explain")
async def explain(payload: ExplainRequest):
    try:
        return {"success": True, "result": explain_concept(payload.topic)}
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))


@app.post("/quiz")
async def quiz(payload: QuizRequest):
    try:
        return {"success": True, "result": generate_quiz(payload.text)}
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))


@app.post("/summarize")
async def summarize(payload: SummaryRequest):
    try:
        return {"success": True, "result": summarize_text(payload.text)}
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))


@app.post("/learn/recommendations")
async def recommendations(payload: LearningPathRequest):
    try:
        return {"success": True, "result": get_learning_recommendations(payload.topic, payload.level)}
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))
