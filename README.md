# 小红书运营中台

基于开源 Skills 的小红书内容运营自动化中台

## 快速开始

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python -m uvicorn api.main:app --reload
```

访问 http://localhost:8000/docs