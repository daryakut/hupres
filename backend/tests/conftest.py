import pytest
from alembic import command
from alembic.config import Config
from sqlalchemy import inspect, text

from database.common import database_engine
from pathlib import Path

current_file = Path(__file__)
relative_path = current_file.relative_to(current_file.parent.parent)

TABLES_TO_AVOID_TRUNCATING = ['alembic_version']


@pytest.fixture(autouse=True, scope='session')
def setup_before_all_tests():
    alembic_ini_path = str(Path(__file__).parent.parent / "alembic.ini")
    alembic_migrations_path = str(Path(__file__).parent.parent / "alembic")
    print(f"Setting up before ALL tests with Alembic at {alembic_ini_path}")
    alembic_cfg = Config(alembic_ini_path)
    alembic_cfg.set_main_option("script_location", alembic_migrations_path)
    command.upgrade(alembic_cfg, "head")


@pytest.fixture(autouse=True, scope='function')
def setup_each_function():
    print("Cleaning the database")
    inspector = inspect(database_engine)
    table_list = [table for table in inspector.get_table_names() if table not in TABLES_TO_AVOID_TRUNCATING]
    comme_separated_table_list = ", ".join(table_list)
    print(f"Truncating tables: {comme_separated_table_list}")
    if len(table_list):
        with database_engine.connect() as conn:
            conn.execute(text(f"TRUNCATE TABLE {comme_separated_table_list} RESTART IDENTITY CASCADE;"))
