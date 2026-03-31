from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import select

from app.api.deps import SessionDep, get_current_active_user
from app.models.entities import Comment, TimeEntry, BoardColumn, Meeting, Document, WorkItem, ProjectMember, User
from app.schemas.common import CommentCreate, TimeEntryCreate, BoardColumnCreate, MeetingCreate, DocumentCreate

router = APIRouter(prefix="/collab", tags=["collaboration"])
CurrentUser = Annotated[User, Depends(get_current_active_user)]


def _project_member(session: SessionDep, user_id: int, project_id: int) -> bool:
    return session.exec(
        select(ProjectMember).where(ProjectMember.project_id == project_id, ProjectMember.user_id == user_id)
    ).first() is not None


@router.post("/comments")
def add_comment(payload: CommentCreate, session: SessionDep, current_user: CurrentUser):
    item = session.get(WorkItem, payload.work_item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Work item not found")
    if not (current_user.is_admin or _project_member(session, current_user.id, item.project_id)):
        raise HTTPException(status_code=403, detail="No access")

    comment = Comment(work_item_id=item.id, author_id=current_user.id, body=payload.body)
    session.add(comment)
    session.commit()
    session.refresh(comment)
    return comment


@router.post("/time-entries")
def add_time_entry(payload: TimeEntryCreate, session: SessionDep, current_user: CurrentUser):
    item = session.get(WorkItem, payload.work_item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Work item not found")
    if not (current_user.is_admin or _project_member(session, current_user.id, item.project_id)):
        raise HTTPException(status_code=403, detail="No access")

    entry = TimeEntry(user_id=current_user.id, **payload.model_dump())
    session.add(entry)
    session.commit()
    session.refresh(entry)
    return entry


@router.post("/board-columns")
def add_board_column(payload: BoardColumnCreate, session: SessionDep, current_user: CurrentUser):
    if not (current_user.is_admin or _project_member(session, current_user.id, payload.project_id)):
        raise HTTPException(status_code=403, detail="No access")
    col = BoardColumn(**payload.model_dump())
    session.add(col)
    session.commit()
    session.refresh(col)
    return col


@router.post("/meetings")
def add_meeting(payload: MeetingCreate, session: SessionDep, current_user: CurrentUser):
    if not (current_user.is_admin or _project_member(session, current_user.id, payload.project_id)):
        raise HTTPException(status_code=403, detail="No access")
    meeting = Meeting(**payload.model_dump())
    session.add(meeting)
    session.commit()
    session.refresh(meeting)
    return meeting


@router.post("/documents")
def add_document(payload: DocumentCreate, session: SessionDep, current_user: CurrentUser):
    if not (current_user.is_admin or _project_member(session, current_user.id, payload.project_id)):
        raise HTTPException(status_code=403, detail="No access")
    doc = Document(**payload.model_dump())
    session.add(doc)
    session.commit()
    session.refresh(doc)
    return doc
