from database.db_answers import DbAnswer
from database.db_question import DbQuestion
from database.db_quiz import DbQuiz
from database.db_quiz_answer import DbQuizAnswer
from database.db_quiz_question import DbQuizQuestion
from database.db_user import DbUser

"""
All DB Entities must be imported here to be included in the database schema.
"""
DB_ENTITIES = [
    DbUser,
    DbQuiz,
    DbQuestion,
    DbAnswer,
    DbQuizQuestion,
    DbQuizAnswer,
]
