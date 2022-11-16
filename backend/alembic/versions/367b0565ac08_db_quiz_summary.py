"""Initial migration

Revision ID: 367b0565ac08
Revises: 3463f0b416db
Create Date: 2023-11-07 02:02:39.052584

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op
from sqlalchemy.sql import expression

# revision identifiers, used by Alembic.
revision: str = '367b0565ac08'
down_revision: Union[str, None] = '3463f0b416db'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('quiz_summaries',
                    sa.Column('id', sa.Integer(), nullable=False, primary_key=True, autoincrement=True),
                    sa.Column('created_at', sa.DateTime, server_default=expression.func.now(), nullable=False),
                    sa.Column('updated_at', sa.DateTime, server_default=expression.func.now(),
                              onupdate=expression.func.now(), nullable=False),
                    sa.Column('quiz_id', sa.Integer(), nullable=False),
                    sa.Column('chart_summary', sa.JSON(), nullable=False),
                    )
    op.create_table('quiz_free_form_questions',
                    sa.Column('id', sa.Integer(), nullable=False, primary_key=True, autoincrement=True),
                    sa.Column('created_at', sa.DateTime, server_default=expression.func.now(), nullable=False),
                    sa.Column('updated_at', sa.DateTime, server_default=expression.func.now(),
                              onupdate=expression.func.now(), nullable=False),
                    sa.Column('quiz_id', sa.Integer(), nullable=False),
                    sa.Column('free_form_question', sa.TEXT(), nullable=False),
                    sa.Column('free_form_answer', sa.TEXT(), nullable=False),
                    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('quiz_summaries')
    op.drop_table('quiz_free_form_questions')
    # ### end Alembic commands ###
