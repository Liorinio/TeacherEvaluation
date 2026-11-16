from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import HTMLResponse
from database.data_access_layer.student_dal import StudentDAL
from database.data_access_layer.score_dal import ScoreDAL
from database.data_access_layer.subject_dal import SubjectDAL
from database.data_access_layer.exam_dal import ExamDAL
from services.teacher_services import add_student_grade
from database.db_dependencies import get_exam_dal, get_score_dal, get_student_dal, get_subject_dal
from services.graph_service import grade_bar_plot, failed_vs_passed

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

@graph_router.get("")
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
