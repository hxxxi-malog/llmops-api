# LLMops

一个基于Flask的LLM应用后端服务框架，提供AI应用管理和对话接口。

## 项目简介

LLMops-API是一个用于管理和部署AI应用的后端服务框架，提供了应用管理、对话接口等核心功能。该框架采用Flask作为Web框架，SQLAlchemy作为ORM，支持依赖注入、数据库迁移等特性。

## 技术栈

- **Web框架**：Flask 3.1.2
- **ORM**：Flask-SQLAlchemy 3.1.1
- **数据库迁移**：Flask-Migrate 4.1.0
- **依赖注入**：Injector 0.22.0
- **表单验证**：Flask-WTF 1.2.2, WTForms 3.2.1
- **LLM集成**：LangChain 1.0.2, LangChain-OpenAI 1.0.1, OpenAI 2.6.1
- **配置管理**：python-dotenv 1.2.1
- **测试框架**：pytest 8.4.2

## 项目结构

```
llmops-api/
├── app/                     # 应用入口
│   ├── http/                # HTTP服务相关
├── config/                  # 配置文件
├── internal/                # 内部模块
│   ├── exception/           # 异常定义
│   ├── extension/           # 扩展模块
│   ├── handler/             # 请求处理器
│   ├── migration/           # 数据库迁移脚本
│   ├── model/               # 数据模型
│   ├── router/              # 路由定义
│   ├── schema/              # 数据验证模式
│   ├── server/              # 服务器定义
│   ├── service/             # 业务逻辑服务
├── pkg/                     # 公共包
│   ├── response/            # 响应格式化
│   ├── sqlalchemy/          # SQLAlchemy扩展
├── storage/                 # 存储目录
├── requirements.txt         # 项目依赖
```

## 安装说明

### 环境要求

- Python 3.8+
- 数据库（支持PostgreSQL，需配置`SQLALCHEMY_DATABASE_URI`）

### 安装步骤

1. 克隆项目

```bash
git clone <repository-url>
cd llmops-api
```

2. 创建虚拟环境

```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
# 或
venv\Scripts\activate  # Windows
```

3. 安装依赖

```bash
pip install -r requirements.txt
```

4. 配置环境变量

创建`.env`文件，配置必要的环境变量：

```
# 数据库连接信息
SQLALCHEMY_DATABASE_URI=postgresql://username:password@localhost:5432/llmops

# SQLAlchemy配置
SQLALCHEMY_POOL_SIZE=30
SQLALCHEMY_POOL_RECYCLE=3600
SQLALCHEMY_ECHO=True

# WTF配置
WTF_CSRF_ENABLED=False

# OpenAI API配置（用于调试接口）
OPENAI_API_KEY=your_api_key_here
```

5. 初始化数据库

```bash
# 运行数据库迁移
flask db upgrade
```

## 快速开始

### 开发模式运行

```bash
python -m app.http.app
```

服务将在`http://localhost:5000`启动。

## API文档

### 1. 调试接口

```
POST /apps/<app_id>/debug
```

**请求体**：
```json
{
  "query": "你好，请介绍一下自己"
}
```

**响应**：
```json
{
  "code": "success",
  "message": "",
  "data": {
    "content": "你好，我是由Malog开发的AI人工智能助手，热心回答一切知道的问题。"
  }
}
```

### 2. 应用管理接口

> 注意：以下接口暂未启用，需要在`router.py`中取消注释

- **创建应用**
  ```
  POST /app
  ```

- **获取应用信息**
  ```
  GET /app/<app_id>
  ```

- **更新应用**
  ```
  POST /app/<app_id>
  ```

- **删除应用**
  ```
  POST /app/<app_id>/delete
  ```

## 开发指南

### 数据库模型

数据模型定义在`internal/model/`目录下，目前包含`App`模型用于存储应用信息。

### 添加新的API接口

1. 在`internal/handler/`目录下创建或更新处理器
2. 在`internal/router/router.py`中注册新路由
3. 如果需要表单验证，在`internal/schema/`中定义验证模式

### 添加新的数据模型

1. 在`internal/model/`目录下创建新的模型类
2. 运行数据库迁移生成脚本
   ```bash
   flask db migrate -m "Add new model"
   ```
3. 应用迁移
   ```bash
   flask db upgrade
   ```

## 异常处理

框架内置了统一的异常处理机制，自定义异常定义在`internal/exception/exception.py`中：

- `CustomException`: 基础异常类
- `FailException`: 操作失败异常
- `NotFoundException`: 资源未找到异常
- `UnauthorizedException`: 未授权异常
- `ForbiddenException`: 禁止访问异常
- `ValidErrorException`: 验证错误异常

## LLM集成

框架集成了LangChain，支持多种LLM模型。目前在调试接口中使用了OpenAI的`qwen3-max`模型，并实现了基于文件的对话历史存储。

## 配置说明

配置文件位于`config/`目录下：

- `config.py`: 主配置类，从环境变量加载配置
- `default_config.py`: 默认配置值

## 部署

### 生产环境建议

1. 使用Gunicorn或uWSGI作为WSGI服务器
2. 配置Nginx作为反向代理
3. 设置适当的数据库连接池大小
4. 关闭调试模式

### 环境变量

生产环境中建议配置以下环境变量：

```
# 关闭调试模式
FLASK_ENV=production

# 数据库配置
SQLALCHEMY_DATABASE_URI=postgresql://username:password@localhost:5432/llmops
SQLALCHEMY_ECHO=False

# 安全配置
SECRET_KEY=your_secret_key_here
WTF_CSRF_ENABLED=True
```

## 许可证

MIT

## 作者

Malog (maloghx@outlook.com)
        