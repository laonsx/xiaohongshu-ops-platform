# 🎯 小红书运营中台

<div align="center">

**基于开源 Skills 的小红书内容运营自动化中台**

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1-green)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

[快速开始](#-快速开始) • [功能特性](#-功能特性) • [文档](#-文档) • [贡献指南](#-贡献指南)

</div>

---

## 📋 项目简介

小红书运营中台是一个全面的内容运营自动化解决方案，集成了小红书官方 API 和开源 Skills，提供了发布、评论、分析等核心功能，帮助运营者高效管理小红书账号。

### 核心价值
- 🚀 **自动化发布**：一键发布笔记，支持批量操作
- 💬 **智能评论**：自动回复、批量评论、情感分析
- 📊 **数据分析**：��时数据洞察、账号健康评估
- 🛡️ **风险预警**：内容审核、账号风险提示
- 🤖 **AI 赋能**：集成 OpenAI，自动生成文案、标签

---

## ✨ 功能特性

### 1. 笔记发布管理
- ✅ 创建和发布笔记
- ✅ 支持多图片上传（最多 9 张）
- ✅ 自动标签提取和推荐
- ✅ 定时发布功能
- ✅ 草稿箱管理

### 2. 评论互动管理
- ✅ 自动获取笔记评论
- ✅ 智能回复评论
- ✅ 批量点赞操作
- ✅ 评论情感分析
- ✅ 用户互动追踪

### 3. 数据分析系统
- ✅ 实时数据统计
- ✅ 账号健康评分
- ✅ 内容效能分析
- ✅ 风险预警机制
- ✅ 数据可视化仪表板

### 4. AI 智能功能
- ✅ 文案自动生成
- ✅ 标签智能推荐
- ✅ 内容风险评估
- ✅ 互动文案建议

### 5. 账号管理
- ✅ 多账号支持
- ✅ 粉丝管理
- ✅ 动态监控
- ✅ 权限管理

---

## 🏗️ 项目架构

```
xiaohongshu-ops-platform/
│
├── backend/                      # 后端服务
│   ├── api/                     # API 层
│   │   ├── main.py             # FastAPI 应用入口
│   │   ├── config.py           # 配置管理
│   │   └── routes/             # 路由模块
│   │       ├── health.py       # 健康检查
│   │       ├── publish.py      # 发布 API
│   │       ├── comments.py     # 评论 API
│   │       └── analytics.py    # 分析 API
│   │
│   ├── models/                 # 数据模型
│   │   └── publish.py          # 发布模型
│   │
│   ├── skills/                 # Skills 集成模块
│   │   ├── xhs_publish/       # 发布 Skill
│   │   ├── xhs_comment/       # 评论 Skill
│   │   └── xhs_analyze/       # 分析 Skill
│   │
│   ├── requirements.txt        # Python 依赖
│   └── .env.example           # 环境变量模板
│
├── docs/                        # 文档
│   ├── SETUP.md               # 详细配置指南
│   ├── QUICK_START.md         # 快速开始指南
│   ├── API_REFERENCE.md       # API 参考文档
│   ├── ARCHITECTURE.md        # 架构设计文档
│   ├── SKILLS_GUIDE.md        # Skills 使用指南
│   └── DEPLOYMENT.md          # 部署指南
│
├── Dockerfile                  # Docker 镜像
├── docker-compose.yml         # Docker 编排配置
├── .gitignore                 # Git 忽略文件
├── README.md                  # 本文件
└── LICENSE                    # MIT 许可证

```

---

## 🚀 快速开始

### 前置要求

- **Python**: 3.9 或更高版本
- **Git**: 用于克隆项目
- **小红书账号**: 需要获取 Cookie
- **OpenAI API Key**: 用于 AI 功能（可选）

### 安装步骤

#### 1️⃣ 克隆项目

```bash
git clone https://github.com/laonsx/xiaohongshu-ops-platform.git
cd xiaohongshu-ops-platform
```

#### 2️⃣ 创建虚拟环境

```bash
cd backend
python3 -m venv venv

# Linux/Mac
source venv/bin/activate

# Windows
venv\Scripts\activate
```

#### 3️⃣ 安装依赖

```bash
pip install -r requirements.txt
```

#### 4️⃣ 配置环境变量

```bash
cp .env.example .env
```

编辑 `.env` 文件，填入必要的配置：

```env
# 小红书配置
XHS_COOKIE=your_cookie_here
XHS_TOKEN=your_token_here

# OpenAI 配置（可选）
OPENAI_API_KEY=sk-your-key-here
OPENAI_MODEL=gpt-4

# 应用配置
DEBUG=True
LOG_LEVEL=INFO
PORT=8000
```

#### 5️⃣ 启动应用

```bash
python -m uvicorn api.main:app --reload
```

#### 6️⃣ 访问应用

- 🌐 **Web 界面**: http://localhost:8000
- 📚 **API 文档**: http://localhost:8000/docs
- 🧪 **API 测试**: http://localhost:8000/redoc

---

## 🐳 Docker 运行

### 使用 Docker

```bash
docker build -t xhs-ops-platform .
docker run -p 8000:8000 --env-file backend/.env xhs-ops-platform
```

### 使用 Docker Compose

```bash
docker-compose up -d
```

查看日志：
```bash
docker-compose logs -f api
```

停止服务：
```bash
docker-compose down
```

---

## 📚 API 示例

### 1. 发布笔记

```bash
curl -X POST http://localhost:8000/api/publish/note \
  -H "Content-Type: application/json" \
  -d '{
    "title": "我的小红书笔记",
    "description": "这是笔记内容描述",
    "images": ["https://example.com/image1.jpg"],
    "topics": ["分享", "生活"],
    "private": false
  }'
```

### 2. 获取评论

```bash
curl http://localhost:8000/api/comments/fetch/7012345678901234567?limit=20
```

### 3. 回复评论

```bash
curl -X POST http://localhost:8000/api/comments/reply \
  -H "Content-Type: application/json" \
  -d '{
    "comment_id": "123456",
    "note_id": "7012345678901234567",
    "reply_text": "感谢您的评论！"
  }'
```

### 4. 分析笔记

```bash
curl -X POST http://localhost:8000/api/analytics/analyze \
  -H "Content-Type: application/json" \
  -d '{
    "note_id": "7012345678901234567",
    "analyze_type": "full"
  }'
```

### 5. 获取仪表板数据

```bash
curl http://localhost:8000/api/analytics/dashboard
```

---

## 🔧 配置指南

### 获取小红书 Cookie

1. 打开 https://www.xiaohongshu.com/
2. 登录您的账号
3. 按 `F12` 打开开发者工具
4. 进入 **Application** → **Cookies**
5. 复制 `Cookie` 字符串
6. 粘贴到 `.env` 文件中

### 获取 OpenAI API Key

1. 访问 https://platform.openai.com/api-keys
2. 创建新的 API Key
3. 复制 API Key
4. 设置到 `.env` 文件中：`OPENAI_API_KEY=sk-...`

> 💡 **提示**: OpenAI 功能是可选的，不配置也可以正常使用基础功能。

---

## 📖 文档

- **[快速开始](./docs/QUICK_START.md)** - 5 分钟快速上手
- **[详细配置](./docs/SETUP.md)** - 环境配置详解
- **[API 参考](./docs/API_REFERENCE.md)** - 完整 API 文档
- **[架构设计](./docs/ARCHITECTURE.md)** - 系统架构详解
- **[Skills 使用](./docs/SKILLS_GUIDE.md)** - Skills 集成指南
- **[部署指南](./docs/DEPLOYMENT.md)** - 生产环境部署

---

## 🛠️ 开发指南

### 项目结构说明

#### API 层 (`backend/api/`)
- 提供 RESTful API 接口
- 使用 FastAPI 框架
- 基于 Pydantic 数据验证

#### 数据模型 (`backend/models/`)
- 定义数据结构
- Pydantic 模型定义
- 数据序列化/反序列化

#### Skills 模块 (`backend/skills/`)
- 业务逻辑实现
- 与小红书 API 交互
- AI 功能集成

### 开发环境

```bash
# 安装开发依赖
pip install -r requirements.txt

# 运行开发服务器
python -m uvicorn api.main:app --reload

# 运行测试
pytest

# 代码格式化
black backend/

# 代码检查
flake8 backend/
```

---

## 🚨 常见问题

### Q: 启动时报错 `ModuleNotFoundError: No module named 'api'`

**A**: 确保您在 `backend` 目录中运行命令：
```bash
cd backend
python -m uvicorn api.main:app --reload
```

### Q: 发布笔记失败，提示 Cookie 无效

**A**: 检查以下事项：
1. Cookie 是否过期，需要重新获取
2. 小红书是否更新了 Cookie 格式
3. 网络连接是否正常

### Q: 如何添加新的 Skill？

**A**: 在 `backend/skills/` 目录下创建新文件夹，参考现有 Skill 的实现方式。

### Q: 支持批量操作吗？

**A**: 目前支持单个操作，批量功能正在开发中。

---

## 🤝 贡献指南

欢迎贡献代码！请遵循以下步骤：

1. **Fork** 本项目
2. **创建** 功能分支 (`git checkout -b feature/AmazingFeature`)
3. **提交** 代码更改 (`git commit -m 'Add some AmazingFeature'`)
4. **推送** 到分支 (`git push origin feature/AmazingFeature`)
5. **提交** Pull Request

### 代码规范

- 使用 PEP 8 风格
- 添加必要的类型提示
- 编写清晰的代码注释
- 提交前运行 `black` 和 `flake8`

---

## 📝 更新日志

### v0.1.0 (2026-07-02)
- ✨ 初始版本发布
- ✨ 基础 API 实现
- ✨ Skills 框架集成
- ✨ 完整文档编写

---

## 📄 许可证

本项目采用 [MIT 许可证](./LICENSE) - 详见 LICENSE 文件

---

## 👨‍💻 作者

**七九** (laonsx)

- 📧 Email: laonsx@163.com
- 🐙 GitHub: [@laonsx](https://github.com/laonsx)

---

## 🌟 致谢

感谢以下项目和社区的支持：

- [FastAPI](https://fastapi.tiangolo.com/) - 现代 Python Web 框架
- [小红书 API](https://www.xiaohongshu.com/) - 内容平台
- [OpenAI API](https://platform.openai.com/) - AI 能力支撑

---

## 📞 联系方式

- 📧 邮件: laonsx@163.com
- 💬 Issues: [GitHub Issues](https://github.com/laonsx/xiaohongshu-ops-platform/issues)
- 💭 讨论: [GitHub Discussions](https://github.com/laonsx/xiaohongshu-ops-platform/discussions)

---

<div align="center">

**如果项目对您有帮助，请 ⭐ Star 一下！**

Made with ❤️ by [laonsx](https://github.com/laonsx)

</div>