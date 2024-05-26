from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, declarative_base

engine = create_engine("sqlite:///database.db")

SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine)

Base = declarative_base()


def get_db():
    database: Session = SessionLocal()
    try:
        yield database
    finally:
        database.close()
