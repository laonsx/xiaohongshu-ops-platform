from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class PublishNote(BaseModel):
    title: str = Field(..., description="笔记标题")
    description: str = Field(..., description="笔记内容")
    images: List[str] = Field(..., description="图片URL列表")
    topics: Optional[List[str]] = None
    private: bool = False
    created_at: datetime = Field(default_factory=datetime.utcnow)