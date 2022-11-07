from database.db_entities.db_quiz import DbQuiz
from database.db_entities.db_quiz_answer import DbQuizAnswer
from database.db_entities.db_quiz_free_form_question import DbQuizFreeFormQuestion
from database.db_entities.db_quiz_question import DbQuizQuestion
from database.db_entities.db_quiz_summary import DbQuizSummary
from database.db_entities.db_user import DbUser

"""
All DB Entities must be imported here to be included in the database schema.
"""
DB_ENTITIES = [
    DbUser,
    DbQuiz,
    DbQuizAnswer,
    DbQuizFreeFormQuestion,
    DbQuizQuestion,
    DbQuizSummary,
]
