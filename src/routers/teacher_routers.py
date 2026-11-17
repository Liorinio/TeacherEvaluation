from datetime import datetime
from fastapi import APIRouter, HTTPException, Depends
from services.administration_services import change_student_grade_level
from src.database.data_access_layer.student_dal import StudentDAL
from src.database.data_access_layer.score_dal import ScoreDAL
from src.services.teacher_services import add_student_grade
from src.database.database_dependencies import get_score_dal, get_student_dal


teacher_router = APIRouter()

@teacher_router.post("/add/grades", tags=['teacher'])
def add_score_to_student(student_id: int, test_name: str, score: int, comments: str, test_date: datetime, grades_db: ScoreDAL = Depends(get_score_dal), student_db: StudentDAL = Depends(get_student_dal)):
    try:
        added_grade = add_student_grade(student_id, test_name, score, comments, test_date, grades_db, student_db)
        if added_grade:
            return {"message": "Added grade successfully", "added grade": added_grade.__str__()}
        else:
            return {"message": "couldn't add grade to the system"}

    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=400, detail=str(error))

teacher_router.patch("")
def change_grade(student_id: int,new_grade_level: str, students_db: StudentDAL= Depends(get_student_dal)):
    try:
        changed_student = change_student_grade_level(student_id, students_db, new_grade_level)
        if changed_student:
            return {"message": "Changed grade successfully", "added grade": changed_student.__str__()}
        else:
            return {"message": "couldn't change the grade level of the given student"}

    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=400, detail=str(error))


