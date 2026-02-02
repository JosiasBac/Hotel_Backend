from pydantic_settings import BaseSettings
from pydantic import ConfigDict


class Settings(BaseSettings):
    app_name: str
    app_env: str
    app_version: str
    database_url: str

    model_config = ConfigDict(env_file=".env")


settings = Settings()
