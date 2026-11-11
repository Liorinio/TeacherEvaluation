from fastapi import APIRouter, HTTPException
from services.administration_services import add_score, add_student, add_subject, add_test,change_student_grade, delete_student, delete_subject, delete_test
from models.student import Student
from models.grade import TestGrade
from models.exam import Exam
from models.subject import Subject
from database.data_access_layer.student_dal import StudentDAL
from database.data_access_layer.score_dal import ScoreDAL
from database.data_access_layer.subject_dal import SubjectDAL
from database.data_access_layer.exam_dal import ExamDAL

admin_router = APIRouter()

@admin_router.post("/add/students", tags=["admin-add"])
def add_student_to_system(student: Student, students_db: StudentDAL | None):
    try:
        added_student = add_student(student, students_db)
        if added_student:
            return {"added student": added_student.__str__()}
        else:
            return {"message": "couldn't add student to the system"}

    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=400, detail=str(error))

@admin_router.post("/add/scores", tags=["admin-add"])
def add_score_to_system(score: TestGrade, score_db: ScoreDAL | None):
    try:
        added_score = add_score(score, score_db)
        if added_score:
            return {"added student": added_score.__str__()}
        else:
            return {"message": "couldn't add score to the system"}

    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=400, detail=str(error))

@admin_router.post("/add/exams", tags=["admin-add"])
def add_exam_to_system(test: Exam, test_db: ExamDAL | None):
    try:
        added_exam = add_test(test, test_db)
        if added_exam:
            return {"added student": added_exam.__str__()}
        else:
            return {"message": "couldn't add test to the system"}

    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=400, detail=str(error))


@admin_router.post("/add/subjects", tags=["admin-add"])
def add_subject_to_system(subject: Subject, subject_db: SubjectDAL | None):
    try:
        added_exam = add_subject(subject, subject_db)
        if added_exam:
            return {"added student": added_exam.__str__()}
        else:
            return {"message": "couldn't add subject to the system"}

    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=400, detail=str(error))

@admin_router.delete("/delete/student", tags=["admin-delete"])
def delete_student_from_system(student_id: int, students_db: StudentDAL | None):
    try:
        added_student = delete_student(student_id, students_db)
        if added_student:
            return {"deleted student": added_student.__str__()}
        else:
            return {"message": "couldn't delete student from the system"}

    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=400, detail=str(error))

@admin_router.delete("/delete/subject", tags=["admin-delete"])
def delete_subject_from_system(student_id: int, subjects_db: SubjectDAL | None):
    try:
        added_subject = delete_subject(student_id, subjects_db)
        if added_subject:
            return {"deleted subject": added_subject.__str__()}
        else:
            return {"message": "couldn't delete subject from the system"}

    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=400, detail=str(error))


@admin_router.delete("/delete/test", tags=["admin-delete"])
def delete_test_from_system(test_id: int, exams_db: ExamDAL | None):
    try:
        added_test = delete_test(test_id, exams_db)
        if added_test:
            return {"deleted test": added_test.__str__()}
        else:
            return {"message": "couldn't delete test from the system"}

    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=400, detail=str(error))
