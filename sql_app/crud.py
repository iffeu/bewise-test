from sqlalchemy.orm import Session

from . import models, schemas

def get_questions(db: Session):
    return db.query(models.Question)

def get_question_by_id(db: Session, question_id: int):
    return db.query(models.Question).filter(models.Question.question_id == question_id).first()

def create_question(db: Session, question: schemas.QuestionCreate):
    db_question = models.Question(question = question.question, answer = question.answer, question_id = question.question_id)
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question
