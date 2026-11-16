from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import HTMLResponse
from src.database.data_access_layer.student_dal import StudentDAL
from src.database.data_access_layer.score_dal import ScoreDAL
from src.database.data_access_layer.subject_dal import SubjectDAL
from src.database.data_access_layer.exam_dal import ExamDAL
from src.services.teacher_services import add_student_grade
from src.database.db_dependencies import get_exam_dal, get_score_dal, get_student_dal, get_subject_dal
from src.services.graph_service import grade_bar_plot, failed_vs_passed, grade_bar_plot_by_class, student_grade_graph

graph_router = APIRouter()


@graph_router.get("/plots/distribution/{test_name}", response_class=HTMLResponse, tags=['graphs'])
def show_grade_distribution(test_name: str, score_dal: ScoreDAL = Depends(get_score_dal)):
    try:
        graph_html = grade_bar_plot(test_name, score_dal)
        if graph_html:
            return HTMLResponse(content=graph_html)
        else:
            return {"message": f"couldn't create a graph of the grades of the following test name: {test_name}"}

    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=400, detail=str(error))

@graph_router.get("/plots/passed-and-failed", response_class=HTMLResponse, tags=['graphs'])
def failed_and_passed_graph(test_name: str, score_dal: ScoreDAL = Depends(get_score_dal)):
    try:
        graph = failed_vs_passed(test_name, score_dal)
        if graph:
            return HTMLResponse(content=graph)
        else:
            return {"message": f"couldn't create a graph of the grades of the following test name: {test_name}"}
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=400, detail=str(error))

@graph_router.get("/plots/distribution/{test_name}/{grade_level}", response_class=HTMLResponse, tags=['graphs'])
def grade_plot_by_class(test_name: str, grade_level: str, grades_db: ScoreDAL = Depends(get_score_dal),
                        students_db: StudentDAL = Depends(get_student_dal)):
    try:
        returning_graph = grade_bar_plot_by_class(test_name, grade_level, grades_db, students_db)
        if returning_graph:
            return HTMLResponse(content=returning_graph)
        else:
            return {"message": f"couldn't create a graph of the grades of the following test name: {test_name} and class {grade_level}"}

    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=400, detail=str(error))

def student_grades_graph(student_id: int, db: ScoreDAL = Depends(get_score_dal)):
    try:
        returned_graph = student_grade_graph(student_id, db)
        if returned_graph:
            return HTMLResponse(content=returned_graph)
        else:
            return {"message": f"couldn't create a graph of the grades of the following student: {student_id}"}
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=400, detail=str(error))


