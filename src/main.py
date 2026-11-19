from fastapi import FastAPI
import uvicorn
from routers.adminestration_routers import admin_router
from routers.graph_routers import graph_router
from routers.stats_router import stats_router
from routers.teacher_routers import teacher_router

app = FastAPI(
    title="Teacher Evaluation API",
    version="1.0.0"
)

