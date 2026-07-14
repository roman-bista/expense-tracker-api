# session.py = How do I connect to the database?
from sqlalchemy import create_engine    #hiring the manager of all database communication.

from sqlalchemy.orm import sessionmaker #sessionmaker is a factory that creates new database Session objects. Each incoming request gets a new Session from this factory.

from app.core.config import settings
