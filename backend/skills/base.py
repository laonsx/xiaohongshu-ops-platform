"""Skills 基类"""

import asyncio
import logging
from typing import Any, Dict, Optional
from abc import ABC, abstractmethod

import httpx
from pydantic import BaseModel


logger = logging.getLogger(__name__)


class SkillConfig(BaseModel):
    """Skill 配置基类"""
    cookie: str
    token: str
    device_id: Optional[str] = None
    timeout: int = 30


class BaseSkill(ABC):
    """Skills 基类"""

    def __init__(self, config: SkillConfig):
        self.config = config
        self.client = httpx.AsyncClient(
            timeout=config.timeout,
            headers=self._build_headers()
        )

    def _build_headers(self) -> Dict[str, str]:
        """构建请求头"""
        return {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Content-Type': 'application/json',
            'Cookie': self.config.cookie,
            'X-Token': self.config.token,
        }

    async def request(
        self,
        method: str,
        url: str,
        **kwargs
    ) -> Dict[str, Any]:
        """发送 HTTP 请求

        Args:
            method: HTTP 方法
            url: 请求 URL
            **kwargs: 其他参数

        Returns:
            响应数据
        """
        try:
            response = await self.client.request(method, url, **kwargs)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            logger.error(f"HTTP 请求失败: {e}")
            raise
        except Exception as e:
            logger.error(f"请求异常: {e}")
            raise

    async def get(self, url: str, **kwargs) -> Dict[str, Any]:
        """GET 请求"""
        return await self.request('GET', url, **kwargs)

    async def post(self, url: str, **kwargs) -> Dict[str, Any]:
        """POST 请求"""
        return await self.request('POST', url, **kwargs)

    async def close(self):
        """关闭客户端"""
        await self.client.aclose()

    @abstractmethod
    async def execute(self, **kwargs) -> Dict[str, Any]:
        """执行 Skill

        Args:
            **kwargs: Skill 参数

        Returns:
            执行结果
        """
        pass

    def __del__(self):
        """析构函数"""
        try:
            asyncio.get_event_loop().run_until_complete(self.close())
        except Exception:
            pass
