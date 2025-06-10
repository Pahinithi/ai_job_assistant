from enum import Enum
from os.path import dirname, realpath

from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class ModelType(str, Enum):
    GPT_3_5_TURBO = "gpt-3.5-turbo"
    GPT_4 = "gpt-4"
    GPT_4O = "gpt-4o-2024-11-20"
    GPT_4_32K = "gpt-4-32k"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        validate_default=False,
        extra="ignore",
    )
    ROOT_DIR: str = realpath(dirname(__file__))
    OPENAI_API_KEY: str


class ScrapeRequest(BaseModel):
    url: str


settings = Settings()
