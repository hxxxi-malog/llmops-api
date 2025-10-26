"""
@Time : 2025/10/26 14:39
@Auth : maloghx@outlook.com
@File : module.py
"""
from injector import Module, Binder

from internal.extension.database_extension import db
from internal.service.app_service import AppService
from internal.handler.app_handler import AppHandler
from pkg.sqlalchemy import SQLAlchemy


class ExtensionModule(Module):
    """扩展模块的依赖注入"""

    def configure(self, binder: Binder) -> None:
        # 绑定 SQLAlchemy 到 db 实例
        binder.bind(SQLAlchemy, to=db)

        # 绑定 AppService（会自动注入 db）
        binder.bind(AppService, to=AppService)

        # 绑定 AppHandler（会自动注入 AppService）
        binder.bind(AppHandler, to=AppHandler)