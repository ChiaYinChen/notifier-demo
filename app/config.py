"""Config."""
from pydantic import BaseSettings


class Settings(BaseSettings):

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
