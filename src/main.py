from fastapi import FastAPI
import uvicorn

from database.database_connection import engine
from database.tables import Base
from routers.adminestration_routers import admin_router
from routers.graph_routers import graph_router
from routers.stats_router import stats_router
from routers.teacher_routers import teacher_router

app = FastAPI(
    title="Teacher Evaluation API",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)

app.include_router(graph_router, prefix="/plots", tags=["plots"])
app.include_router(admin_router, prefix="/admin", tags=["admin"])
app.include_router(stats_router, prefix="/stats", tags=["stats"])
app.include_router(teacher_router, prefix="/teacher", tags=["teacher"])


@app.get("/heath_check")
def heath_check():
    return {"satus: running"}

if __name__ == "__main__":
    uvicorn.run(app="main:app", host="127.0.0.1", port=8080, reload=True)