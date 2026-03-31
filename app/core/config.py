from pydantic import BaseModel


class Settings(BaseModel):
    app_name: str = "Work Management API"
    jwt_secret: str = "change-me"
    jwt_algorithm: str = "HS256"
    access_token_expire_minutes: int = 60 * 24
    database_url: str = "sqlite:///./app.db"


settings = Settings()
