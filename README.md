# Work Management API (Python)

Backend em Python (FastAPI) para uma plataforma de gestão de projetos inspirada no OpenProject.

## Stack
- FastAPI
- SQLModel + SQLite
- JWT (python-jose)
- Passlib (bcrypt)

## Banco de dados (SQLite)
A aplicação usa **SQLite** por padrão no arquivo:
- `./data/work_management.db`

A URL padrão fica em `app/core/config.py`:
- `sqlite:///./data/work_management.db`

## Como rodar
```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
uvicorn app.main:app --reload
```

A API sobe em `http://127.0.0.1:8000`.

## Seed de dados
```bash
python seed.py
```

Usuários seed:
- `admin@example.com` / `admin123`
- `member@example.com` / `member123`

## Endpoints principais
- `POST /auth/register`
- `POST /auth/login`
- `POST /projects`
- `GET /projects`
- `POST /projects/{project_id}/members/{user_id}?role=member`
- `POST /work-items`
- `GET /work-items/project/{project_id}`
- `PATCH /work-items/{work_item_id}/status`
- `POST /collab/comments`
- `POST /collab/time-entries`
- `POST /collab/board-columns`
- `POST /collab/meetings`
- `POST /collab/documents`

## Observações
Este commit entrega uma base funcional completa de backend modular em Python para os módulos principais (identidade, projetos, work items, board, tempo, documentos e reuniões), pronta para evolução com frontend e recursos avançados.
