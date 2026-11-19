from fastapi import APIRouter, HTTPException, Depends
from src.database.data_access_layer.score_dal import ScoreDAL
from src.database.database_dependencies import get_score_dal
from services.statistics.stats_service import median_of_a_test, avg_of_a_test, percent_25th_of_a_test, percent_75th_of_a_test

stats_router = APIRouter()

@stats_router.get("/avg/{test_name}")
def test_average(test_name: str, score_dal: ScoreDAL = Depends(get_score_dal)):
    try:
        test_avg = avg_of_a_test(test_name, score_dal)
        if test_avg:
            return {"message": f"Calculates average successfully", "average": test_avg}
        else:
            return {"message": f"Couldn't calculates average for the following test: {test_name}"}

    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=400, detail=str(error))

@stats_router.get("/avg/{test_name}")
def test_median(test_name: str, score_dal: ScoreDAL = Depends(get_score_dal)):
    try:
        test_med = median_of_a_test(test_name, score_dal)
        if test_med:
            return {"message": f"Calculates average successfully", "median": test_med}
        else:
            return {"message": f"Couldn't calculates average for the following test: {test_name}"}

    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=400, detail=str(error))

@stats_router.get("/med/{test_name}")
def test_median(test_name: str, score_dal: ScoreDAL = Depends(get_score_dal)):
    try:
        test_med = median_of_a_test(test_name, score_dal)
        if test_med:
            return {"message": f"Calculates average successfully", "median": test_med}
        else:
            return {"message": f"Couldn't calculates average for the following test: {test_name}"}

    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=400, detail=str(error))


@stats_router.get("/percent/25th/{test_name}")
def test_percent_25th(test_name: str, score_dal: ScoreDAL = Depends(get_score_dal)):
    try:
        test_25th_percent = percent_25th_of_a_test(test_name, score_dal)
        if test_25th_percent:
            return {"message": f"Calculates average successfully", "median": test_25th_percent}
        else:
            return {"message": f"Couldn't calculates average for the following test: {test_name}"}

    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=400, detail=str(error))

@stats_router.get("/percent/75th/{test_name}")
def test_percent_75th(test_name: str, score_dal: ScoreDAL = Depends(get_score_dal)):
    try:
        test_25th_percent = percent_75th_of_a_test(test_name, score_dal)
        if test_25th_percent:
            return {"message": f"Calculates average successfully", "median": test_25th_percent}
        else:
            return {"message": f"Couldn't calculates average for the following test: {test_name}"}

    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=400, detail=str(error))