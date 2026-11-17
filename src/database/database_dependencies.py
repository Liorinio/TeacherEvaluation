from fastapi import Depends
from sqlalchemy.orm import Session
from typing import Generator
from src.database.data_access_layer.student_dal import StudentDAL
from src.database.data_access_layer.exam_dal import ExamDAL
from src.database.data_access_layer.score_dal import ScoreDAL
from src.database.data_access_layer.subject_dal import SubjectDAL
from src.database.database_connection import SessionLocal

def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_student_dal(db: Session = Depends(get_db)) -> StudentDAL:
    return StudentDAL(db)

def get_subject_dal(db: Session = Depends(get_db)) -> SubjectDAL:
    return SubjectDAL(db)

def get_exam_dal(db: Session = Depends(get_db)) -> ExamDAL:
    return ExamDAL(db)

def get_score_dal(db: Session = Depends(get_db)) -> ScoreDAL:
    return ScoreDAL(db)