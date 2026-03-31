from fastapi import FastAPI

from app.api import auth, projects, work_items, collab
from app.core.db import init_db

app = FastAPI(title="Work Management API", version="0.1.0")


@app.on_event("startup")
def on_startup():
    init_db()


@app.get("/health")
def health():
    return {"status": "ok"}


app.include_router(auth.router)
app.include_router(projects.router)
app.include_router(work_items.router)
app.include_router(collab.router)
