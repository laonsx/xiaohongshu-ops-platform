"""小红书评论 Skill 实现"""

import logging
from typing import Any, Dict, List, Optional

from ..base import BaseSkill, SkillConfig
from .models import CommentRequest, CommentResponse


logger = logging.getLogger(__name__)


class CommentSkill(BaseSkill):
    """小红书评论 Skill

    用于获取评论、发布评论、点赞评论等功能
    """

    API_BASE_URL = "https://edith.xiaohongshu.com"

    async def get_comments(
        self,
        note_id: str,
        limit: int = 30,
        offset: int = 0,
        sort: str = 'hot'
    ) -> Dict[str, Any]:
        """获取笔记评论

        Args:
            note_id: 笔记 ID
            limit: 返回评论数量
            offset: 偏移量
            sort: 排序方式 (hot/new)

        Returns:
            评论列表
        """
        try:
            params = {
                'note_id': note_id,
                'limit': limit,
                'offset': offset,
                'sort': sort,
            }
            url = f"{self.API_BASE_URL}/web_api/v1/feed/{note_id}/comments"
            response = await self.get(url, params=params)
            logger.info(f"获取评论成功: {note_id}")
            return response
        except Exception as e:
            logger.error(f"获取评论失败: {e}")
            raise

    async def publish_comment(
        self,
        note_id: str,
        comment_text: str,
        image_list: Optional[List[str]] = None,
        at_user_id: Optional[str] = None,
    ) -> CommentResponse:
        """发布评论

        Args:
            note_id: 笔记 ID
            comment_text: 评论文本
            image_list: 图片列表
            at_user_id: @用户 ID

        Returns:
            发布响应
        """
        try:
            comment_data = {
                'note_id': note_id,
                'content': comment_text,
                'interact_info': '',
            }

            if image_list:
                comment_data['image_list'] = await self._upload_images(image_list)

            if at_user_id:
                comment_data['at_user_id'] = at_user_id

            url = f"{self.API_BASE_URL}/web_api/v1/feed/{note_id}/comments"
            response = await self.post(url, json=comment_data)

            if response.get('success'):
                comment_id = response.get('data', {}).get('comment_id')
                logger.info(f"评论发布成功，ID: {comment_id}")
                return CommentResponse(
                    success=True,
                    comment_id=comment_id,
                    message="评论发布成功",
                    timestamp=str(response.get('timestamp', ''))
                )
            else:
                error_msg = response.get('msg', '未知错误')
                logger.error(f"评论发布失败: {error_msg}")
                return CommentResponse(
                    success=False,
                    message=f"发布失败: {error_msg}",
                    timestamp=str(response.get('timestamp', ''))
                )

        except Exception as e:
            logger.error(f"发布评论异常: {e}")
            return CommentResponse(
                success=False,
                message=f"发布异常: {str(e)}",
                timestamp=""
            )

    async def reply_comment(
        self,
        note_id: str,
        comment_id: str,
        reply_text: str,
        image_list: Optional[List[str]] = None,
    ) -> CommentResponse:
        """回复评论

        Args:
            note_id: 笔记 ID
            comment_id: 评论 ID
            reply_text: 回复文本
            image_list: 图片列表

        Returns:
            回复响应
        """
        try:
            reply_data = {
                'note_id': note_id,
                'comment_id': comment_id,
                'content': reply_text,
            }

            if image_list:
                reply_data['image_list'] = await self._upload_images(image_list)

            url = f"{self.API_BASE_URL}/web_api/v1/feed/{note_id}/comments/{comment_id}/replies"
            response = await self.post(url, json=reply_data)

            if response.get('success'):
                reply_id = response.get('data', {}).get('reply_id')
                logger.info(f"回复发布成功，ID: {reply_id}")
                return CommentResponse(
                    success=True,
                    comment_id=reply_id,
                    message="回复发布成功",
                    timestamp=str(response.get('timestamp', ''))
                )
            else:
                error_msg = response.get('msg', '未知错误')
                return CommentResponse(
                    success=False,
                    message=f"发布失败: {error_msg}",
                    timestamp=str(response.get('timestamp', ''))
                )

        except Exception as e:
            logger.error(f"回复评论异常: {e}")
            return CommentResponse(
                success=False,
                message=f"回复异常: {str(e)}",
                timestamp=""
            )

    async def like_comment(
        self,
        note_id: str,
        comment_id: str,
    ) -> Dict[str, Any]:
        """点赞评论

        Args:
            note_id: 笔记 ID
            comment_id: 评论 ID

        Returns:
            点赞结果
        """
        try:
            url = f"{self.API_BASE_URL}/web_api/v1/feed/{note_id}/comments/{comment_id}/like"
            response = await self.post(url, json={'action': 'like'})
            logger.info(f"评论点赞成功: {comment_id}")
            return response
        except Exception as e:
            logger.error(f"点赞评论失败: {e}")
            raise

    async def unlike_comment(
        self,
        note_id: str,
        comment_id: str,
    ) -> Dict[str, Any]:
        """取消点赞评论

        Args:
            note_id: 笔记 ID
            comment_id: 评论 ID

        Returns:
            取消点赞结果
        """
        try:
            url = f"{self.API_BASE_URL}/web_api/v1/feed/{note_id}/comments/{comment_id}/like"
            response = await self.post(url, json={'action': 'unlike'})
            logger.info(f"取消评论点赞成功: {comment_id}")
            return response
        except Exception as e:
            logger.error(f"取消点赞失败: {e}")
            raise

    async def delete_comment(
        self,
        note_id: str,
        comment_id: str,
    ) -> Dict[str, Any]:
        """删除评论

        Args:
            note_id: 笔记 ID
            comment_id: 评论 ID

        Returns:
            删除结果
        """
        try:
            url = f"{self.API_BASE_URL}/web_api/v1/feed/{note_id}/comments/{comment_id}"
            response = await self.post(url, json={'action': 'delete'})
            logger.info(f"评论删除成功: {comment_id}")
            return response
        except Exception as e:
            logger.error(f"删除评论失败: {e}")
            raise

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
                uploaded_images.append({
                    'url': url,
                    'size': 0,
                    'index': idx
                })
            except Exception as e:
                logger.warning(f"上传图片失败 {url}: {e}")
        return uploaded_images

    async def execute(self, **kwargs) -> Dict[str, Any]:
        """执行评论 Skill

        Args:
            **kwargs: 包含 action 和其他参数

        Returns:
            执行结果
        """
        action = kwargs.get('action', 'get_comments')

        if action == 'get_comments':
            return await self.get_comments(
                note_id=kwargs.get('note_id'),
                limit=kwargs.get('limit', 30),
                offset=kwargs.get('offset', 0),
                sort=kwargs.get('sort', 'hot'),
            )
        elif action == 'publish':
            result = await self.publish_comment(
                note_id=kwargs.get('note_id'),
                comment_text=kwargs.get('comment_text'),
                image_list=kwargs.get('image_list'),
                at_user_id=kwargs.get('at_user_id'),
            )
            return result.dict()
        elif action == 'reply':
            result = await self.reply_comment(
                note_id=kwargs.get('note_id'),
                comment_id=kwargs.get('comment_id'),
                reply_text=kwargs.get('reply_text'),
                image_list=kwargs.get('image_list'),
            )
            return result.dict()
        elif action == 'like':
            return await self.like_comment(
                note_id=kwargs.get('note_id'),
                comment_id=kwargs.get('comment_id'),
            )
        elif action == 'unlike':
            return await self.unlike_comment(
                note_id=kwargs.get('note_id'),
                comment_id=kwargs.get('comment_id'),
            )
        elif action == 'delete':
            return await self.delete_comment(
                note_id=kwargs.get('note_id'),
                comment_id=kwargs.get('comment_id'),
            )
        else:
            raise ValueError(f"未知的操作: {action}")
