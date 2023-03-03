"""Config."""
from pydantic import BaseSettings


class Settings(BaseSettings):

    SLACK_WEBHOOK_URL: str
    SLACK_USERNAME: str = "webhook-bot"
    SLACK_ICON_EMOJI: str = ":ghost:"

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
