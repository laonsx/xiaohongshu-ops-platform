# 配置指南

## 环境要求

- Python 3.9+
- pip 或 conda
- Git
- 小红书账号

## 获取小红书 Cookie

1. 打开 https://www.xiaohongshu.com/
2. 登录账号
3. 按 F12 打开开发者工具
4. 进入 Application → Cookies
5. 复制整个 Cookie 值
6. 粘贴到 `.env` 文件

## 配置 OpenAI API

1. 访问 https://platform.openai.com/api-keys
2. 创建 API Key
3. 在 `.env` 中填入 `OPENAI_API_KEY=sk-...`

## 本地开发

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# 编辑 .env
python -m uvicorn api.main:app --reload
```