from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
import datetime

from .database import Base

def default_datetime():
    return datetime.datetime.now()

class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    question_id = Column(Integer, index=True)
    question = Column(String, index=True)
    answer = Column(String, index=True)
    created_at = Column(DateTime, default=default_datetime, nullable=False)

