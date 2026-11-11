from sqlalchemy import delete
from sqlalchemy.orm import Session
from models.grade import TestGrade


class ScoreDAL:
    def __init__(self, db: Session):
        self.db = db

    def delete_exam_by_id(self, test_name, student_id):
        stmt = delete(TestGrade).where(TestGrade.test_name==test_name).where(TestGrade.student_id==student_id)
        self.db.execute(stmt)
        self.db.commit()

    def add_grade(self, grade: TestGrade):
        existing_score = self.db.query(TestGrade).filter_by(student_id=grade.student_id).filter_by(test_name=grade.test_name).first()

        if existing_score:
            raise ValueError("The grade is already in the data-storage")

        self.db.add(grade)
        self.db.commit()
        self.db.refresh(grade)

        return grade

    def get_grade_by_score_id(self, test_name, student_id):
        return self.db.query(TestGrade).filter_by(student_id=student_id).filter_by(test_name=test_name).first()

    def get_grades_by_test_name(self, test_name: str):
        return self.db.query(TestGrade).filter_by(test_name=test_name).all()

    def get_grade_by_student_id(self, student_id):
        return self.db.query(TestGrade).filter_by(student_id=student_id).all()