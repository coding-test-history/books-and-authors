from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME:str
    APP_DESC:str
    APP_VERSION:str
    APP_HOST:str
    APP_PORT:int
    APP_RELOAD:bool
    DB_CONNECTION: str
    DB_HOST: str
    DB_PORT: int
    DB_DATABASE: str
    DB_USERNAME: str
    DB_PASSWORD: str

    class Config:
        env_file = ".env"

settings = Settings()
