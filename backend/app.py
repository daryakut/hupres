"""
Application definition
"""

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

from sqlalchemy import create_engine, Column, Integer, String, Sequence, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from database.transaction import transaction
from quiz_algorithm.models import Quiz

app = FastAPI()

# # Base = declarative_base()
#
# # class User(Base):
# #     __tablename__ = 'users'
# #     id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
# #     name = Column(String(50))
# #     age = Column(Integer)
#
# DATABASE_URL = "postgresql+psycopg2://georgii:@localhost/georgii"
#
# engine = create_engine(DATABASE_URL)
#
# # Create tables in the database (only need to run this once)
# # Base.metadata.create_all(engine)
#
# # To start a new session and interact with the database
# Session = sessionmaker(bind=engine)
# session = Session()


@app.get("/")
async def home():
    with transaction() as session:
        current_timestamp = session.query(func.now()).scalar()
        return HTMLResponse(f"Hello world! {current_timestamp}")
    # return HTMLResponse("Hello world!")


@app.get("/404")
async def missing():
    return HTMLResponse("That's gonna be a 'no' from me.", status_code=404)


class CreateQuizResponse(BaseModel):
    quiz: Quiz


@app.post("/quizzes")
async def create_quiz() -> CreateQuizResponse:

    return CreateQuizResponse(quiz=Quiz())


class CreateQuizResponse(BaseModel):
    quiz: Quiz


@app.post("/users")
async def create_user() -> CreateQuizResponse:

    return CreateQuizResponse(quiz=Quiz())
