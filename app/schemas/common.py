from datetime import date
from typing import Optional

from pydantic import BaseModel, EmailStr

from app.models.entities import ProjectStatus, WorkItemStatus


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class UserCreate(BaseModel):
    email: EmailStr
    full_name: str
    password: str


class UserRead(BaseModel):
    id: int
    email: EmailStr
    full_name: str
    is_active: bool
    is_admin: bool


class ProjectCreate(BaseModel):
    name: str
    description: str = ""


class ProjectRead(BaseModel):
    id: int
    name: str
    description: str
    status: ProjectStatus
    owner_id: int


class WorkItemCreate(BaseModel):
    title: str
    description: str = ""
    project_id: int
    assignee_id: Optional[int] = None
    priority: str = "medium"
    start_date: Optional[date] = None
    due_date: Optional[date] = None


class WorkItemRead(BaseModel):
    id: int
    title: str
    description: str
    project_id: int
    assignee_id: Optional[int]
    status: WorkItemStatus
    priority: str


class WorkItemStatusUpdate(BaseModel):
    status: WorkItemStatus


class TimeEntryCreate(BaseModel):
    work_item_id: int
    hours: float
    activity: str = "development"


class CommentCreate(BaseModel):
    work_item_id: int
    body: str


class BoardColumnCreate(BaseModel):
    project_id: int
    name: str
    order: int = 0


class MeetingCreate(BaseModel):
    project_id: int
    title: str
    agenda: str = ""


class DocumentCreate(BaseModel):
    project_id: int
    name: str
    category: str = "general"
    url: str
