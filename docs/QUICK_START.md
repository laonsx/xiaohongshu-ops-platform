# 快速开始

只需 5 分钟即可启动！

```bash
git clone https://github.com/laonsx/xiaohongshu-ops-platform.git
cd xiaohongshu-ops-platform/backend

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
cp .env.example .env

# 编辑 .env 填入 Cookie 和 API Key
python -m uvicorn api.main:app --reload
```

访问 http://localhost:8000/docs