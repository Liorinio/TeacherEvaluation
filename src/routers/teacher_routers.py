from datetime import datetime
from fastapi import APIRouter, HTTPException, Depends
from src.database.data_access_layer.student_dal import StudentDAL
from src.database.data_access_layer.score_dal import ScoreDAL
from src.database.data_access_layer.subject_dal import SubjectDAL
from src.database.data_access_layer.exam_dal import ExamDAL
from src.services.teacher_services import add_student_grade
from src.database.db_dependencies import get_exam_dal, get_score_dal, get_student_dal, get_subject_dal


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

