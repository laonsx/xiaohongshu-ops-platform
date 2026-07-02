"""评论 Skill 数据模型"""

from typing import Optional, List
from pydantic import BaseModel, Field


class CommentRequest(BaseModel):
    """评论请求模型"""
    note_id: str = Field(..., description="笔记 ID")
    comment_text: str = Field(..., description="评论文本")
    image_list: Optional[List[str]] = Field(default=None, description="图片列表")


class CommentResponse(BaseModel):
    """评论响应模型"""
    success: bool = Field(..., description="是否成功")
    comment_id: Optional[str] = Field(default=None, description="评论 ID")
    message: str = Field(..., description="响应消息")
    timestamp: str = Field(..., description="时间戳")


class Comment(BaseModel):
    """评论信息模型"""
    comment_id: str = Field(..., description="评论 ID")
    user_id: str = Field(..., description="用户 ID")
    user_name: str = Field(..., description="用户名")
    avatar: str = Field(..., description="头像")
    content: str = Field(..., description="评论内容")
    create_time: int = Field(..., description="创建时间")
    like_count: int = Field(default=0, description="点赞数")
    reply_count: int = Field(default=0, description="回复数")
    status: int = Field(..., description="评论状态")
