from sqlalchemy import delete
from sqlalchemy.orm import Session
from models.student import Student

class StudentDAL:
    def __init__(self, db: Session):
        self.db = db

    def get_student_by_id(self, student_id: int):
        return self.db.query(Student).filter_by(student_id=student_id).first()

    def get_student_by_name(self, student_name: int):
        return self.db.query(Student).filter_by(student_name=student_name).first()

    def delete_student_by_id(self, student_id):
        existing_student = self.db.query(Student).filter_by(student_id=student_id).first()

        if not existing_student:
            raise ValueError("The student is already deleted from the database")

        stmt = delete(Student).where(Student.student_id == student_id)
        self.db.execute(stmt)
        self.db.commit()

    def add_student(self, student: Student):
        existing_student = self.db.query(Student).filter_by(student_id=student.student_id).first()

        if existing_student:
            raise ValueError("The student is already in the database")

        self.db.add(student)
        self.db.commit()
        self.db.refresh(student)

        return student

    def get_students_by_class(self, grade_level: str):
        return self.db.query(Student).filter_by(grade_level=grade_level).all()

    def change_student_grade(self, student_id: int, new_grade: str):
        existing_student = self.get_student_by_id(student_id)

        if not existing_student:
            raise ValueError("The student isn't in the database")

        existing_student.set_grade_level(new_grade)
        self.db.commit()
        self.db.refresh(existing_student)
