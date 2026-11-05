from datetime import datetime
from database.data_access_layer.score_dal import ScoreDAL
from database.data_access_layer.student_dal import StudentDAL
from models.grade import TestGrade


def add_student_grade(student_id: int, test_name: str, score: int, comments: str, test_date: datetime, grades_db: ScoreDAL | None, student_db: StudentDAL | None):
    if grades_db is not None and student_db is not None:
        student = student_db.get_student_by_id(student_id)
        if not student:
            raise ValueError(f"Student with ID {student_id} not found.")

        student_grade = grades_db.get_grade_by_score_id(student_id, test_name)
        if not student_grade:
            raise ValueError(f"score of student with ID {student_id} is already exists.")

        test_grade = TestGrade(student_id, test_name, score, comments, test_date)
        is_grade_added = grades_db.add_grade(test_grade)

        if is_grade_added:
            print("added")  # TODO: change to log
            return is_grade_added
        else:
            print("already in db")  # TODO: change to log
            return None

    return None

