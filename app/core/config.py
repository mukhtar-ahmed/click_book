import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',env_ignore_empty=True,extra='ignore'
    )
    DB_URL: str 
    print("DB_URL from env:", os.environ.get("DB_URL"))


settings = Settings()