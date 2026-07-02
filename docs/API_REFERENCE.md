# API 参考文档

## 基础信息

- Base URL: `http://localhost:8000/api`
- Response Format: JSON

## 端点列表

### GET /health

检查应用健康状态

### POST /publish/note

发布笔记

**Request:**
```json
{
  "title": "笔记标题",
  "description": "笔记内容",
  "images": ["https://example.com/1.jpg"],
  "topics": ["标签"],
  "private": false
}
```

### GET /comments/fetch/{note_id}

获取评论

### POST /comments/reply

回复评论

### POST /analytics/analyze

分析笔记

### GET /analytics/dashboard

获取仪表板数据

详见浏览器访问 http://localhost:8000/docs