from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    USER_NAME: str
    USER_PASSWORD: str
    USER_HOST: str
    USER_DATABASE: str
    USER_PORT: int

    class Config:
        env_file = './.env'


settings = Settings()
