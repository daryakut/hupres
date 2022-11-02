"""Initial migration

Revision ID: 3463f0b416db
Revises: 
Create Date: 2023-11-01 15:47:20.463334

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from database.db_types.token_db_type import TokenDbType
from database.db_types.string_enum_db_type import StringEnumDbType
from quizzes.quiz_steps import QuizStep, QuizSubStep
from models.quiz_models import UserRole

# revision identifiers, used by Alembic.
revision: str = '3463f0b416db'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('questions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('token', sa.String(length=32), nullable=True),
    sa.Column('question_name', sa.String(length=100), nullable=True),
    sa.Column('is_tablet', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('token')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('token', TokenDbType(length=64), nullable=True),
    sa.Column('email_address', sa.String(), nullable=False),
    sa.Column('role', StringEnumDbType(UserRole), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('token')
    )
    op.create_table('answers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('token', sa.String(length=32), nullable=True),
    sa.Column('question_id', sa.Integer(), nullable=True),
    sa.Column('answer_name', sa.String(length=100), nullable=True),
    sa.Column('sign_scores', sa.JSON(), nullable=True),
    sa.ForeignKeyConstraint(['question_id'], ['questions.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('token')
    )
    op.create_table('quizzes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('token', sa.String(length=32), nullable=True),
    sa.Column('session_token', sa.String(length=100), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.Column('subject_name', sa.String(length=100), nullable=True),
    sa.Column('pronounce', sa.String(length=50), nullable=True),
    sa.Column('dm_after_step_1', sa.String(length=10), nullable=True),
    sa.Column('dm_after_step_2', sa.String(length=10), nullable=True),
    sa.Column('dm_after_step_3', sa.String(length=10), nullable=True),
    sa.Column('dm_after_step_4', sa.String(length=10), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('token')
    )
    op.create_table('quiz_questions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('token', sa.String(length=32), nullable=True),
    sa.Column('quiz_id', sa.Integer(), nullable=True),
    sa.Column('question_name', sa.String(length=50), nullable=True),
    sa.Column('quiz_step', StringEnumDbType(QuizStep), nullable=True),
    sa.Column('quiz_substep', StringEnumDbType(QuizSubStep), nullable=True),
    sa.Column('followup_question_signs', sa.JSON(), nullable=True),
    sa.ForeignKeyConstraint(['quiz_id'], ['quizzes.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('token')
    )
    op.create_table('quiz_answers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('token', sa.String(length=32), nullable=True),
    sa.Column('quiz_id', sa.Integer(), nullable=True),
    sa.Column('quiz_question_id', sa.Integer(), nullable=True),
    sa.Column('answer_name', sa.String(length=50), nullable=True),
    sa.Column('is_all_zeros', sa.Boolean(), nullable=True),
    sa.Column('current_sign_scores', sa.JSON(), nullable=True),
    sa.Column('original_sign_scores', sa.JSON(), nullable=True),
    sa.Column('signs_for_next_questions', sa.JSON(), nullable=True),
    sa.ForeignKeyConstraint(['quiz_id'], ['quizzes.id'], ),
    sa.ForeignKeyConstraint(['quiz_question_id'], ['quiz_questions.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('token')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('quiz_answers')
    op.drop_table('quiz_questions')
    op.drop_table('quizzes')
    op.drop_table('answers')
    op.drop_table('users')
    op.drop_table('questions')
    # ### end Alembic commands ###