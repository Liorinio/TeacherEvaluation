from database.data_access_layer.exam_dal import ExamDAL
from database.data_access_layer.score_dal import ScoreDAL
from database.data_access_layer.student_dal import StudentDAL
from database.data_access_layer.subject_dal import SubjectDAL
from models.exam import Exam
from models.grade import TestGrade
from models.student import Student
from models.subject import Subject
import logging

logger = logging.getLogger(__name__)


def add_student(student: Student, students_db: StudentDAL | None):
    if students_db is not None:
        added_student = students_db.add_student(student)
        return added_student
    return None


def delete_student(student_id: int, students_db: StudentDAL | None):
    if students_db is not None:
        students_db.delete_student_by_id(student_id)
        logger.info("student was deleted")


def change_student_grade(student_id: int, students_db: StudentDAL | None, new_grade: str):
    if students_db is not None:
        students_db.change_student_grade(student_id, new_grade)


def add_subject(subject: Subject, subject_db: SubjectDAL | None):
    if subject_db is not None:
        added_subject = subject_db.add_subject(subject)
        return added_subject
    return None


def delete_subject(subject_id: int, subject_db: SubjectDAL | None):
    if subject_db is not None:
        subject_db.delete_subject_by_id(subject_id)
        logger.info("subject was deleted")


def add_test(test: Exam, test_db: ExamDAL | None):
    if test_db is not None:
        added_test = test_db.add_exam(test)
        return added_test
    return None


def delete_test(test_id: int, test_db: ExamDAL | None):
    if test_db is not None:
        test_db.delete_exam_by_id(test_id)
        logger.info("exam was deleted")


def add_score(score: TestGrade, score_db: ScoreDAL | None):
    if score_db is not None:
        added_score = score_db.add_grade(score)
        return added_score
    return None
