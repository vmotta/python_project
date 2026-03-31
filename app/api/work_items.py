from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import select

from app.api.deps import SessionDep, get_current_active_user
from app.models.entities import WorkItem, ProjectMember, User
from app.schemas.common import WorkItemCreate, WorkItemRead, WorkItemStatusUpdate

router = APIRouter(prefix="/work-items", tags=["work-items"])
CurrentUser = Annotated[User, Depends(get_current_active_user)]


def _has_project_access(session: SessionDep, user: User, project_id: int) -> bool:
    if user.is_admin:
        return True
    member = session.exec(
        select(ProjectMember).where(ProjectMember.project_id == project_id, ProjectMember.user_id == user.id)
    ).first()
    return member is not None


@router.post("", response_model=WorkItemRead)
def create_work_item(payload: WorkItemCreate, session: SessionDep, current_user: CurrentUser):
    if not _has_project_access(session, current_user, payload.project_id):
        raise HTTPException(status_code=403, detail="No access to project")

    item = WorkItem(**payload.model_dump())
    session.add(item)
    session.commit()
    session.refresh(item)
    return item


@router.get("/project/{project_id}", response_model=list[WorkItemRead])
def list_work_items(project_id: int, session: SessionDep, current_user: CurrentUser):
    if not _has_project_access(session, current_user, project_id):
        raise HTTPException(status_code=403, detail="No access to project")
    return list(session.exec(select(WorkItem).where(WorkItem.project_id == project_id)).all())


@router.patch("/{work_item_id}/status", response_model=WorkItemRead)
def update_status(work_item_id: int, payload: WorkItemStatusUpdate, session: SessionDep, current_user: CurrentUser):
    item = session.get(WorkItem, work_item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Work item not found")
    if not _has_project_access(session, current_user, item.project_id):
        raise HTTPException(status_code=403, detail="No access to project")

    item.status = payload.status
    session.add(item)
    session.commit()
    session.refresh(item)
    return item
