from sqlmodel import Session, select

from app.core.db import engine, init_db
from app.core.security import hash_password
from app.models.entities import User, Project, ProjectMember, WorkItem


def run_seed() -> None:
    init_db()
    with Session(engine) as session:
        if session.exec(select(User)).first():
            print("Seed already applied")
            return

        admin = User(
            email="admin@example.com",
            full_name="Admin",
            hashed_password=hash_password("admin123"),
            is_admin=True,
        )
        member = User(
            email="member@example.com",
            full_name="Member",
            hashed_password=hash_password("member123"),
        )
        session.add(admin)
        session.add(member)
        session.commit()
        session.refresh(admin)
        session.refresh(member)

        project = Project(name="Projeto Exemplo", description="Projeto seed", owner_id=admin.id)
        session.add(project)
        session.commit()
        session.refresh(project)

        session.add(ProjectMember(project_id=project.id, user_id=admin.id, role="owner"))
        session.add(ProjectMember(project_id=project.id, user_id=member.id, role="member"))
        session.add(WorkItem(title="Planejar sprint", project_id=project.id, assignee_id=member.id))
        session.commit()

        print("Seed applied with default users")


if __name__ == "__main__":
    run_seed()
