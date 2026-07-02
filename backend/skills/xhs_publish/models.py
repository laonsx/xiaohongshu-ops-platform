"""发布 Skill 数据模型"""

from typing import List, Optional
from pydantic import BaseModel, Field


class PublishRequest(BaseModel):
    """发布请求模型"""
    title: str = Field(..., description="笔记标题")
    description: str = Field(..., description="笔记描述")
    images: Optional[List[str]] = Field(default=None, description="图片 URL 列表")
    topics: Optional[List[str]] = Field(default=None, description="话题标签")
    location: Optional[str] = Field(default=None, description="位置信息")
    private: bool = Field(default=False, description="是否私密笔记")
    interact_info: Optional[str] = Field(default=None, description="互动信息")


class PublishResponse(BaseModel):
    """发布响应模型"""
    success: bool = Field(..., description="是否成功")
    note_id: Optional[str] = Field(default=None, description="笔记 ID")
    message: str = Field(..., description="响应消息")
    timestamp: str = Field(..., description="时间戳")


class NoteInfo(BaseModel):
    """笔记信息模型"""
    note_id: str = Field(..., description="笔记 ID")
    title: str = Field(..., description="笔记标题")
    desc: str = Field(..., description="笔记描述")
    create_time: int = Field(..., description="创建时间")
    interact_info: Optional[dict] = Field(default=None, description="互动信息")
