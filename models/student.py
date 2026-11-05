from datetime import datetime


class Student:
    student_id: int
    student_name: str
    grade_level : str
    enroll_date = datetime

    def __init__(self, student_id: int, student_name: str, grade_level: str, enroll_date: datetime):
        self.student_id = student_id
        self.student_name = student_name
        self.grade_level = grade_level
        self.enroll_date = enroll_date

    def get_student_id(self):
        return self.student_id

    def get_name(self):
        return self.student_name

    def set_student_name(self, student_name: str):
        self.student_name = student_name

    def set_grade_level(self, grade_level: str):
        self.grade_level = grade_level
