from datetime import datetime, date
from enum import Enum
from typing import Optional

from sqlmodel import SQLModel, Field


class ProjectStatus(str, Enum):
    active = "active"
    archived = "archived"


class WorkItemStatus(str, Enum):
    todo = "todo"
    in_progress = "in_progress"
    done = "done"
    blocked = "blocked"


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(index=True, unique=True)
    full_name: str
    hashed_password: str
    is_active: bool = True
    is_admin: bool = False


class Project(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    description: str = ""
    status: ProjectStatus = ProjectStatus.active
    owner_id: int = Field(foreign_key="user.id")


class ProjectMember(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    project_id: int = Field(foreign_key="project.id", index=True)
    user_id: int = Field(foreign_key="user.id", index=True)
    role: str = "member"


class WorkItem(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(index=True)
    description: str = ""
    project_id: int = Field(foreign_key="project.id", index=True)
    assignee_id: Optional[int] = Field(default=None, foreign_key="user.id")
    status: WorkItemStatus = WorkItemStatus.todo
    priority: str = "medium"
    start_date: Optional[date] = None
    due_date: Optional[date] = None
    parent_id: Optional[int] = Field(default=None, foreign_key="workitem.id")


class TimeEntry(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id", index=True)
    work_item_id: int = Field(foreign_key="workitem.id", index=True)
    hours: float
    activity: str = "development"
    entry_date: date = Field(default_factory=date.today)


class Comment(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    work_item_id: int = Field(foreign_key="workitem.id", index=True)
    author_id: int = Field(foreign_key="user.id")
    body: str
    created_at: datetime = Field(default_factory=datetime.utcnow)


class BoardColumn(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    project_id: int = Field(foreign_key="project.id", index=True)
    name: str
    order: int = 0


class Meeting(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    project_id: int = Field(foreign_key="project.id", index=True)
    title: str
    agenda: str = ""
    notes: str = ""
    meeting_date: date = Field(default_factory=date.today)


class Document(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    project_id: int = Field(foreign_key="project.id", index=True)
    name: str
    category: str = "general"
    url: str
