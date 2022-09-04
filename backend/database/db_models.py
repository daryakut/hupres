from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, JSON
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class DbUser(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    token = Column(String, unique=True)
    email_address = Column(String)
    role = Column(String)


class DbQuestion(Base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True)
    token = Column(String, unique=True)
    question_name = Column(String)
    is_tablet = Column(Boolean)


class DbAnswer(Base):
    __tablename__ = 'answers'
    id = Column(Integer, primary_key=True)
    token = Column(String, unique=True)
    question_id = Column(Integer, ForeignKey('questions.id'))
    answer_name = Column(String)
    sign_scores = Column(JSON)


class DbQuiz(Base):
    __tablename__ = 'quizzes'
    id = Column(Integer, primary_key=True)
    token = Column(String, unique=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    subject_name = Column(String)
    pronounce = Column(String)
    dm_after_step_1 = Column(String)
    dm_after_step_2 = Column(String)
    dm_after_step_3 = Column(String)
    dm_after_step_4 = Column(String)


class DbQuizQuestion(Base):
    __tablename__ = 'quiz_questions'
    id = Column(Integer, primary_key=True)
    token = Column(String, unique=True)
    quiz_id = Column(Integer, ForeignKey('quizzes.id'))
    question_id = Column(Integer, ForeignKey('questions.id'))
    quiz_step = Column(Integer)
    quiz_substep = Column(Integer)
    followup_question_signs = Column(JSON)


class DbQuizAnswer(Base):
    __tablename__ = 'quiz_answers'
    id = Column(Integer, primary_key=True)
    token = Column(String, unique=True)
    quiz_id = Column(Integer, ForeignKey('quizzes.id'))
    quiz_question_id = Column(Integer, ForeignKey('quiz_questions.id'))
    answer_id = Column(Integer, ForeignKey('answers.id'))
    current_sign_scores = Column(JSON)
    original_sign_scores = Column(JSON)
