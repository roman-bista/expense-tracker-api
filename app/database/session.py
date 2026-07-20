# session.py = How do I connect to the database?
from sqlalchemy import create_engine   #hiring the manager of all database communication.
from sqlalchemy.orm import sessionmaker,Session #sessionmaker is a factory that creates new database Session objects. Each incoming request gets a new Session from this factory.

from app.core.config import settings
from fastapi import Depends


engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(bind=engine,
                            autoflush=False,
                            autocommit=False)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
        

