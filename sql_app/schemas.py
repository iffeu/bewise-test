from pydantic import BaseModel
import datetime

class QuestionBase(BaseModel):
    question: str
    answer: str

class QuestionCreate(BaseModel):
    questions_num: int

class Question(QuestionBase):
    created_at: datetime.datetime
    question_id: int
    id: int
    class Config:
        from_attributes = True
