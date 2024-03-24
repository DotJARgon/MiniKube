from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from apiRest import databaseConfig

DATABASE_USERNAME = databaseConfig.DATABASE_USERNAME
DATABASE_PASSWORD = databaseConfig.DATABASE_PASSWORD
DATABASE_HOST = databaseConfig.DATABASE_HOST
DATABASE_NAME = databaseConfig.DATABASE_NAME
DATABASE_PORT = databaseConfig.DATABASE_PORT

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE_NAME}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
