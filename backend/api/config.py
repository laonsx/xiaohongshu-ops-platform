from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    app_name: str = "xiaohongshu-ops-platform"
    app_version: str = "0.1.0"
    debug: bool = False
    port: int = 8000
    xhs_cookie: Optional[str] = None
    xhs_token: Optional[str] = None
    openai_api_key: Optional[str] = None
    openai_model: str = "gpt-4"
    
    class Config:
        env_file = ".env"
        case_sensitive = False

settings = Settings()