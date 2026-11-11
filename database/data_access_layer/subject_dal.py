from sqlalchemy import delete
from sqlalchemy.orm import Session
from models.subject import Subject

class SubjectDAL:
    def __init__(self, db: Session):
        self.db = db

    def delete_subject_by_id(self, subject_id):
        existing_subject = self.db.query(Subject).filter_by(subject_id=subject_id).first()

        if not existing_subject:
            raise ValueError("The subject is already deleted from the database")

        stmt = delete(Subject).where(Subject.subject_id == subject_id)
        self.db.execute(stmt)
        self.db.commit()

    def add_subject(self, subject: Subject):
        existing_subject = self.db.query(Subject).filter_by(student_id=subject.subject_id).first()

        if existing_subject:
            raise ValueError("The subject is already in the data-storage")

        self.db.add(subject)
        self.db.commit()
        self.db.refresh(subject)

        return subject

    def get_subject_by_name(self, subject_name: str):
        return self.db.query(Subject).filter_by(subject_name=subject_name).first()



