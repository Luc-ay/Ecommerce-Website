from pydantic_settings import BaseSettings

class SecretConfig(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    class Config:
        env_file = ".env"

secret = SecretConfig()  # type: ignore