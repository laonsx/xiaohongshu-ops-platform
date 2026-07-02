"""分析 Skill 数据模型"""

from typing import Optional, Dict, Any, List
from pydantic import BaseModel, Field


class AnalyzeRequest(BaseModel):
    """分析请求模型"""
    note_id: str = Field(..., description="笔记 ID")
    analyze_type: str = Field(default='basic', description="分析类型")


class AnalyzeResponse(BaseModel):
    """分析响应模型"""
    success: bool = Field(..., description="是否成功")
    data: Optional[Dict[str, Any]] = Field(default=None, description="分析数据")
    message: str = Field(..., description="响应消息")


class NoteAnalysis(BaseModel):
    """笔记分析模型"""
    note_id: str = Field(..., description="笔记 ID")
    title: str = Field(..., description="笔记标题")
    view_count: int = Field(..., description="浏览数")
    like_count: int = Field(..., description="点赞数")
    comment_count: int = Field(..., description="评论数")
    share_count: int = Field(..., description="分享数")
    collect_count: int = Field(..., description="收藏数")
    engagement_rate: float = Field(..., description="互动率")
    trend: Optional[Dict[str, List[int]]] = Field(default=None, description="趋势数据")


class UserStats(BaseModel):
    """用户统计模型"""
    user_id: str = Field(..., description="用户 ID")
    total_notes: int = Field(..., description="笔记总数")
    total_followers: int = Field(..., description="粉丝数")
    avg_engagement: float = Field(..., description="平均互动率")
    popular_topics: List[str] = Field(..., description="热门话题")
    account_health: float = Field(..., description="账号健康度")
