import os

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

from common.env import env, EnvStage

# import psycopg2
# db_connection = psycopg2.connect(dbname='georgii', user="georgii", password="", host='localhost', port=5432)
# print("Successfully connected to the database.")

# username = "hupres"
# password = "123456"
# hostname = "localhost"
# port = "5432"
# database_name = "hupres_test"
username = os.environ.get('HUPRES_POSTGRES_USERNAME')
password = os.environ.get('HUPRES_POSTGRES_PASSWORD')
hostname = os.environ.get('HUPRES_POSTGRES_HOSTNAME')
port = os.environ.get('HUPRES_POSTGRES_PORT')
database_name = os.environ.get('HUPRES_POSTGRES_DATABASE_NAME')

if env.stage == EnvStage.TEST:
    # Just in case make sure we only run tests in the test environment
    assert username == "hupres"
    assert password == "123456"
    assert hostname == "localhost"
    assert port == "5432"
    assert database_name == "hupres_test"

print("DB", hostname)

DATABASE_URL = f"postgresql+psycopg2://{username}:{password}@{hostname}:{port}/{database_name}"
# _DATABASE_URL = "postgresql+psycopg2://georgii@localhost:5432/georgii"

DbBase = declarative_base()
database_engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=database_engine)
