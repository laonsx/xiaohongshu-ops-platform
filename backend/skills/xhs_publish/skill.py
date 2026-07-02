"""小红书发布 Skill 实现"""

import asyncio
import logging
from typing import Any, Dict, List, Optional

from ..base import BaseSkill, SkillConfig
from .models import PublishRequest, PublishResponse


logger = logging.getLogger(__name__)


class PublishSkill(BaseSkill):
    """小红书发布 Skill

    用于发布笔记、管理草稿等功能
    """

    API_BASE_URL = "https://edith.xiaohongshu.com"

    async def publish_note(
        self,
        title: str,
        description: str,
        images: Optional[List[str]] = None,
        topics: Optional[List[str]] = None,
        location: Optional[str] = None,
        private: bool = False,
        interact_info: Optional[str] = None,
    ) -> PublishResponse:
        """发布笔记

        Args:
            title: 笔记标题
            description: 笔记描述
            images: 图片 URL 列表
            topics: 话题标签
            location: 位置信息
            private: 是否私密笔记
            interact_info: 互动信息

        Returns:
            发布响应
        """
        try:
            # 构建笔记数据
            note_data = {
                'title': title,
                'desc': description,
                'type': 'normal',
                'topic': topics or [],
                'poi_info': location or '',
                'interact_info': interact_info or '',
                'is_private': private,
            }

            # 处理图片
            if images:
                note_data['image_list'] = await self._upload_images(images)

            # 发送请求
            url = f"{self.API_BASE_URL}/web_api/v1/feed"
            response = await self.post(url, json={'note': note_data})

            if response.get('success'):
                note_id = response.get('data', {}).get('note_id')
                logger.info(f"笔记发布成功，ID: {note_id}")
                return PublishResponse(
                    success=True,
                    note_id=note_id,
                    message="笔记发布成功",
                    timestamp=str(response.get('timestamp', ''))
                )
            else:
                error_msg = response.get('msg', '未知错误')
                logger.error(f"笔记发布失败: {error_msg}")
                return PublishResponse(
                    success=False,
                    message=f"发布失败: {error_msg}",
                    timestamp=str(response.get('timestamp', ''))
                )

        except Exception as e:
            logger.error(f"发布笔记异常: {e}")
            return PublishResponse(
                success=False,
                message=f"发布异常: {str(e)}",
                timestamp=""
            )

    async def _upload_images(self, image_urls: List[str]) -> List[Dict[str, Any]]:
        """上传图片

        Args:
            image_urls: 图片 URL 列表

        Returns:
            图片信息列表
        """
        uploaded_images = []
        for idx, url in enumerate(image_urls):
            try:
                # 从 URL 下载图片
                response = await self.get(url)
                # 这里简化处理，实际需要上传到小红书服务器
                uploaded_images.append({
                    'url': url,
                    'size': 0,
                    'index': idx
                })
            except Exception as e:
                logger.warning(f"上传图片失败 {url}: {e}")
        return uploaded_images

    async def get_draft(
        self,
        draft_id: str
    ) -> Dict[str, Any]:
        """获取草稿

        Args:
            draft_id: 草稿 ID

        Returns:
            草稿信息
        """
        try:
            url = f"{self.API_BASE_URL}/web_api/v1/draft/{draft_id}"
            response = await self.get(url)
            logger.info(f"获取草稿成功: {draft_id}")
            return response
        except Exception as e:
            logger.error(f"获取草稿失败: {e}")
            raise

    async def save_draft(
        self,
        title: str,
        description: str,
        images: Optional[List[str]] = None,
        topics: Optional[List[str]] = None,
    ) -> Dict[str, Any]:
        """保存草稿

        Args:
            title: 标题
            description: 描述
            images: 图片列表
            topics: 话题

        Returns:
            保存结果
        """
        try:
            draft_data = {
                'title': title,
                'desc': description,
                'topic': topics or [],
                'image_list': images or [],
            }
            url = f"{self.API_BASE_URL}/web_api/v1/draft"
            response = await self.post(url, json={'draft': draft_data})
            logger.info("草稿保存成功")
            return response
        except Exception as e:
            logger.error(f"保存草稿失败: {e}")
            raise

    async def delete_draft(self, draft_id: str) -> Dict[str, Any]:
        """删除草稿

        Args:
            draft_id: 草稿 ID

        Returns:
            删除结果
        """
        try:
            url = f"{self.API_BASE_URL}/web_api/v1/draft/{draft_id}"
            response = await self.post(url, json={'action': 'delete'})
            logger.info(f"草稿删除成功: {draft_id}")
            return response
        except Exception as e:
            logger.error(f"删除草稿失败: {e}")
            raise

    async def execute(self, **kwargs) -> Dict[str, Any]:
        """执行发布 Skill

        Args:
            **kwargs: 包含 action 和其他参数

        Returns:
            执行结果
        """
        action = kwargs.get('action', 'publish')

        if action == 'publish':
            result = await self.publish_note(
                title=kwargs.get('title'),
                description=kwargs.get('description'),
                images=kwargs.get('images'),
                topics=kwargs.get('topics'),
                location=kwargs.get('location'),
                private=kwargs.get('private', False),
            )
            return result.dict()
        elif action == 'save_draft':
            return await self.save_draft(
                title=kwargs.get('title'),
                description=kwargs.get('description'),
                images=kwargs.get('images'),
                topics=kwargs.get('topics'),
            )
        elif action == 'get_draft':
            return await self.get_draft(draft_id=kwargs.get('draft_id'))
        elif action == 'delete_draft':
            return await self.delete_draft(draft_id=kwargs.get('draft_id'))
        else:
            raise ValueError(f"未知的操作: {action}")
