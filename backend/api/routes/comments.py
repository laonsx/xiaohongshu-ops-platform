from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

router = APIRouter()

class ReplyRequest(BaseModel):
    comment_id: str
    note_id: str
    reply_text: str = Field(..., min_length=1, max_length=500)

@router.get("/comments/fetch/{note_id}")
async def fetch_comments(note_id: str, limit: Optional[int] = 20):
    try:
        return {
            "success": True,
            "note_id": note_id,
            "comments": [],
            "total": 0,
            "limit": limit
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/comments/reply")
async def reply_comment(request: ReplyRequest):
    try:
        return {
            "success": True,
            "reply_id": "789012",
            "message": "回复已发送",
            "timestamp": datetime.utcnow().isoformat()
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))