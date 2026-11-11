from fastapi import APIRouter, HTTPException
from services.administration_services import add_score, add_student, add_subject, add_test,change_student_grade, delete_student, delete_subject, delete_test
from models.student import Student
from database.data_access_layer.student_dal import StudentDAL

admin_router = APIRouter()

admin_router.post("/add/students")
def add_student_to_system(student: Student, students_db: StudentDAL | None):
    try:
        added_student = add_student(student, students_db)
        if added_student:
            return {"added student": added_student.__str__()}
        else:
            return {"couldn't add student to the system"}

    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=400, detail=str(error))
