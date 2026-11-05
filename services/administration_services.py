from database.data_access_layer.student_dal import StudentDAL
from models.student import Student
import logging

logger = logging.getLogger(__name__)

def add_student(student: Student, students_db: StudentDAL | None):
    if students_db is not None:
        students_db.add_student(student)

def delete_student(student_id: int, students_db: StudentDAL | None):
    if students_db is not None:
        students_db.delete_student_by_id(student_id)
        logger.info("student was deleted")

def change_student_grade(student_id: int, students_db: StudentDAL | None, new_grade: str):
    if students_db is not None:
        students_db.change_student_grade(student_id,new_grade)