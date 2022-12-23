from pydantic import BaseSettings


class Settings(BaseSettings):
    db_url: str = "sqlite:///backend.db"

    class Config:
        env_file = ".env"
