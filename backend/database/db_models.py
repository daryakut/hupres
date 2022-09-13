from __future__ import annotations

from sqlalchemy import Enum as SQLEnum
from sqlalchemy import ForeignKey, Column, Integer, String, Boolean
from sqlalchemy import JSON
from sqlalchemy.orm import relationship, backref

from database.common import DbBase, Session
from quiz_algorithm.common import first_or_none
from quiz_algorithm.constants import Sign
from quiz_algorithm.models import UserRole, Pronounce, User, Question, Answer, Quiz


class DbUser(DbBase):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    token = Column(String(32), unique=True)
    email_address = Column(String, nullable=False)
    role = Column(String(50), nullable=False)

    def to_model(self) -> User:
        return User(
            token=self.token,
            email_address=self.email_address,
            role=UserRole(self.role)
        )

    @staticmethod
    def create_user(session: Session, email_address: str, role: UserRole) -> DbUser:
        db_user = DbUser(email_address=email_address, role=role.value)
        session.add(db_user)
        return db_user


class DbQuestion(DbBase):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True)
    token = Column(String(32), unique=True)
    question_name = Column(String(100))
    is_tablet = Column(Boolean)

    answers = relationship('DbAnswer', back_populates='question', lazy='select')

    def to_model(self) -> Question:
        return Question(
            token=self.token,
            question_name=self.question_name,
            is_tablet=self.is_tablet
        )


class DbAnswer(DbBase):
    __tablename__ = 'answers'
    id = Column(Integer, primary_key=True)
    token = Column(String(32), unique=True)
    question_id = Column(Integer, ForeignKey('questions.id'))
    answer_name = Column(String(100))
    sign_scores = Column(JSON)

    question = relationship('DbQuestion', backref=backref('answers', lazy=True))

    def to_model(self) -> Answer:
        return Answer(
            token=self.token,
            question_token=self.question.token,
            answer_name=self.answer_name,
            sign_scores=self.sign_scores
        )


class DbQuiz(DbBase):
    __tablename__ = 'quizzes'
    id = Column(Integer, primary_key=True)
    token = Column(String(32), unique=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    subject_name = Column(String(100))
    pronounce = Column(String(50))
    dm_after_step_1 = Column(String(10))
    dm_after_step_2 = Column(String(10))
    dm_after_step_3 = Column(String(10))
    dm_after_step_4 = Column(String(10))

    user = relationship('DbUser', lazy='select')
    quiz_questions = relationship('DbQuizQuestion', back_populates='quiz', lazy='select')
    quiz_answers = relationship('DbQuizAnswer', back_populates='quiz', lazy='select')

    def to_model(self) -> Quiz:
        return Quiz(
            token=self.token,
            user_token=self.user.token,
            subject_name=self.subject_name,
            pronounce=Pronounce(self.pronounce),
            dm_after_step_1=Sign(self.dm_after_step_1),
            dm_after_step_2=Sign(self.dm_after_step_2),
            dm_after_step_3=Sign(self.dm_after_step_3),
            dm_after_step_4=Sign(self.dm_after_step_4)
        )


class DbQuizQuestion(DbBase):
    __tablename__ = 'quiz_questions'
    id = Column(Integer, primary_key=True)
    token = Column(String(32), unique=True)
    quiz_id = Column(Integer, ForeignKey('quizzes.id'))
    question_id = Column(Integer, ForeignKey('questions.id'))
    quiz_step = Column(Integer)
    quiz_substep = Column(Integer)
    followup_question_signs = Column(JSON)

    quiz = relationship(DbQuiz.__name__, back_populates='questions', lazy='select')
    question = relationship(DbQuestion.__name__, lazy='select')

    # there should be max one answer per question, so we expose it via property
    __quiz_answers = relationship('DbQuizAnswer', back_populates='quiz_question', lazy='select')

    @property
    def answer(self) -> DbAnswer:
        quiz_answers = self.__quiz_answers
        if len(quiz_answers) > 1:
            raise ValueError('QuizQuestion has more than one answer')
        return first_or_none(quiz_answers)


class DbQuizAnswer(DbBase):
    __tablename__ = 'quiz_answers'
    id = Column(Integer, primary_key=True)
    token = Column(String(32), unique=True)
    quiz_id = Column(Integer, ForeignKey('quizzes.id'))
    quiz_question_id = Column(Integer, ForeignKey('quiz_questions.id'))
    answer_id = Column(Integer, ForeignKey('answers.id'))
    current_sign_scores = Column(JSON)
    original_sign_scores = Column(JSON)

    quiz = relationship(DbQuiz.__name__, back_populates='questions', lazy='select')
    quiz_question = relationship('DbQuizQuestion', back_populates='__quiz_answers', lazy='select')
    answer = relationship(DbAnswer.__name__, lazy='select')
