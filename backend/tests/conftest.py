import pytest
from alembic import command
from alembic.config import Config
from sqlalchemy import inspect
from sqlalchemy.engine import reflection

from database.common import database_engine
from pathlib import Path

current_file = Path(__file__)
relative_path = current_file.relative_to(current_file.parent.parent)


@pytest.fixture(autouse=True, scope='session')
def setup_before_all_tests():
    print(f"Setting up before ALL tests with Alembic at {str(Path(__file__).parent.parent / 'alembic.ini')}")
    alembic_cfg = Config(str(Path(__file__).parent.parent / "alembic.ini"))
    command.upgrade(alembic_cfg, "head")


@pytest.fixture(autouse=True, scope='function')
def setup_each_function():
    print("Cleaning the database")
    inspector = inspect(database_engine)
    table_list = inspector.get_table_names()
    print(table_list)
    # with database_engine.connect() as conn:
    #     conn.execute("TRUNCATE TABLE table1, table2, table3 RESTART IDENTITY CASCADE;")
