from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

load_dotenv()

from api.routes import health, publish, comments, analytics

app = FastAPI(
    title="小红书运营中台 API",
    description="基于开源 Skills 的小红书内容运营自动化平台",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router, prefix="/api", tags=["Health"])
app.include_router(publish.router, prefix="/api", tags=["Publish"])
app.include_router(comments.router, prefix="/api", tags=["Comments"])
app.include_router(analytics.router, prefix="/api", tags=["Analytics"])

@app.get("/")
async def root():
    return {
        "message": "欢迎使用小红书运营中台 🎉",
        "version": "0.1.0",
        "docs": "/docs"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api.main:app", host="0.0.0.0", port=8000, reload=True)