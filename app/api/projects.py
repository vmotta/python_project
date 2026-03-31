from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import select

from app.api.deps import SessionDep, get_current_active_user
from app.models.entities import Project, ProjectMember, User
from app.schemas.common import ProjectCreate, ProjectRead

router = APIRouter(prefix="/projects", tags=["projects"])
CurrentUser = Annotated[User, Depends(get_current_active_user)]


@router.post("", response_model=ProjectRead)
def create_project(payload: ProjectCreate, session: SessionDep, current_user: CurrentUser):
    project = Project(name=payload.name, description=payload.description, owner_id=current_user.id)
    session.add(project)
    session.commit()
    session.refresh(project)

    session.add(ProjectMember(project_id=project.id, user_id=current_user.id, role="owner"))
    session.commit()
    return project


@router.get("", response_model=list[ProjectRead])
def list_projects(session: SessionDep, current_user: CurrentUser):
    memberships = session.exec(select(ProjectMember).where(ProjectMember.user_id == current_user.id)).all()
    project_ids = [m.project_id for m in memberships]
    if not project_ids and not current_user.is_admin:
        return []

    query = select(Project)
    if not current_user.is_admin:
        query = query.where(Project.id.in_(project_ids))
    return list(session.exec(query).all())


@router.post("/{project_id}/members/{user_id}")
def add_member(project_id: int, user_id: int, role: str, session: SessionDep, current_user: CurrentUser):
    project = session.get(Project, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    if project.owner_id != current_user.id and not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Only owner/admin can add members")

    if not session.get(User, user_id):
        raise HTTPException(status_code=404, detail="User not found")

    membership = ProjectMember(project_id=project_id, user_id=user_id, role=role)
    session.add(membership)
    session.commit()
    return {"message": "Member added"}
