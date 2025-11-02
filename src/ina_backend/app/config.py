from pydantic import  AnyUrl
from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    DATABASE_URL_DEV: str
    DATABASE_URL_TEST: str
    DATABASE_URL_PROD: str
    SECRET_KEY: str
    ALGORITHM: str 
    ACCESS_TOKEN_EXPIRE_MINUTES: int 
    CORS_ORIGINS: str 

    class Config:
        env_file = ".env"

settings = Settings()
