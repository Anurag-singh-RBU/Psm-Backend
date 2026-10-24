from typing import Literal

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy import URL

Env = Literal["dev", "prod"]

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file = ".env.dev",
        validate_default = True, 
        case_sensitive = False
    )

    app_env: Env
    app_name: str = "XPIRE"
    app_version: str = "1.0.0"

    db_host: str
    db_server: int = 5432
    db_name: str
    db_user: str
    db_secret: SecretStr

    @property
    def database_url(self) -> URL:
        return URL.create(
            drivername = "postgresql+asyncpg",
            username = self.db_user,
            password = self.db_secret.get_secret_value(),
            host = self.db_host,
            port = self.db_server,
            database = self.db_name,
        )

def get_settings() -> Settings:
    return Settings()

