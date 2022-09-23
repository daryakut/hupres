from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# import psycopg2
# db_connection = psycopg2.connect(dbname='georgii', user="georgii", password="", host='localhost', port=5432)
# print("Successfully connected to the database.")

username = "hupres"
password = "123456"
hostname = "localhost"
port = "5432"
database_name = "hupres_test"

DATABASE_URL = f"postgresql+psycopg2://{username}:{password}@{hostname}:{port}/{database_name}"
# _DATABASE_URL = "postgresql+psycopg2://georgii@localhost:5432/georgii"

DbBase = declarative_base()
database_engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=database_engine)