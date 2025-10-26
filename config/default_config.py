"""
@Time : 2025/10/26 14:22
@Auth : maloghx@outlook.com
@File : default_config.py
"""

DEFAULT_CONFIG = {
    # wtf csrf
    "WTF_CSRF_ENABLED": "False",
    # SQLAlchemy 默认配置
    "SQLALCHEMY_DATABASE_URI": "",
    "SQLALCHEMY_POOL_SIZE": 30,
    "SQLALCHEMY_POOL_RECYCLE": 3600,
    "SQLALCHEMY_ECHO": "True"
}
