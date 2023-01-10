from datetime import datetime
from pathlib import Path

from platformdirs import os
from sqlalchemy import Column, DateTime, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# BASE_DIR = os.path.dirname(os.path.realpath(__file__))
BASE_DIR = Path(__file__).resolve().parent.parent
connection_string = 'sqlite:///'+os.path.join(BASE_DIR, 'sqlite.db')
engine = create_engine(connection_string, echo=True)

Session = sessionmaker()

class User(Base):
    __tablename__='users'
    id = Column(Integer(), primary_key=True)
    username = Column(String(25), nullable=False, unique=True)
    email = Column(String(80), nullable=False, unique=True)
    date_created = Column(DateTime(), default=datetime.utcnow)

    def __repr__(self):
        return self.username
