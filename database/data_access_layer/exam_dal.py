from sqlalchemy import delete
from sqlalchemy.orm import Session
from models.exam import Exam


class ExamDAL:
    def __init__(self, db: Session):
        self.db = db

    def delete_exam_by_id(self, test_title):
        stmt = delete(Exam).where(Exam.test_title==test_title)
        self.db.execute(stmt)
        self.db.commit()

    def add_exam(self, exam: Exam):
        existing_subject = self.db.query(Exam).filter_by(test_title=exam.test_title).first()

        if existing_subject:
            raise ValueError("The exam is already in the data-storage")

        self.db.add(exam)
        self.db.commit()
        self.db.refresh(exam)

        return exam

    def get_exam_by_name(self, exam_name: str):
        return self.db.query(Exam).filter_by(test_title=exam_name).first()



