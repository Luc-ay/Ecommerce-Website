from pydantic_settings import BaseSettings

class SecretConfig(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str

    class Config:
        env_file = ".env"

secret = SecretConfig()  # type: ignore