from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

from quiz_algorithm.models import Quiz

router = APIRouter()


class CreateQuizResponse(BaseModel):
    quiz: Quiz


@router.get("/quizzes/hello")
async def create_quiz() -> HTMLResponse:
    return HTMLResponse("Das quiz")


@router.post("/quizzes")
async def create_quiz() -> CreateQuizResponse:
    return CreateQuizResponse(quiz=Quiz())
