from fastapi import Depends, FastAPI, HTTPException, Response, status
from sqlalchemy.orm import Session
import requests as rq
import json

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/questions/", response_model=list[schemas.Question])
def read_questions(db: Session = Depends(get_db)):
    questions = crud.get_questions(db)
    return questions

@app.post("/questions/", response_model=schemas.Question)
def create_question(question: schemas.QuestionCreate, db: Session = Depends(get_db)):
    last_question: Question = db.query(models.Question).order_by(models.Question.id.desc()).first()
    
    remaining_questions: int = question.questions_num
    while remaining_questions:
        base_url: str = "https://jservice.io/api/random?count="
        response: Response = rq.get(base_url + f'{remaining_questions}')
        response_dict: dict = json.loads(response.text)
        for question in response_dict:
            question_exists_in_db: Question = crud.get_question_by_id(db, question_id = question['id'])
            if question_exists_in_db:
                continue
            remaining_questions -= 1
            crud.create_question(db=db, question = models.Question(question = question['question'], answer = question['answer'], question_id=question['id']))
    if last_question == None:
        return Response(status_code=status.HTTP_200_OK)
    else:
        return last_question
