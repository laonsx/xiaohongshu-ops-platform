from fastapi import APIRouter
from datetime import datetime

router = APIRouter()

@router.get("/health")
async def health_check():
    return {
        "status": "ok",
        "message": "小红书运营中台正在运行中",
        "version": "0.1.0",
        "timestamp": datetime.utcnow().isoformat()
    }