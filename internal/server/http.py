"""
@Time : 2025/10/25 19:37
@Auth : maloghx@outlook.com
@File : http.py
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import Config
from internal.router import Router
from internal.exception import CustomException
from pkg.response import Response, json, HttpCode


class Http(Flask):
    """Http 服务引擎"""

    def __init__(self, *args, conf: Config, db: SQLAlchemy, router: Router, **kwargs):
        super().__init__(*args, **kwargs)
        # 从配置对象中加载应用配置
        self.config.from_object(conf)

        # 注册全局异常处理函数，将所有Exception类型的异常都交给self._register_error_handler方法
        self.register_error_handler(Exception, self._register_error_handler)

        # 初始化flask拓展
        db.init_app(self)

        # 注册应用录路由
        router.register_router(self)

    def _register_error_handler(self, error: Exception):
        # 处理自定义异常
        if isinstance(error, CustomException):
            return json(Response(
                code=error.code,
                message=error.message,
                data=error.data if error.data is not None else {},
            ))

        # 调试模式下直接抛出异常，否则返回统一错误响应
        if self.debug:
            raise error
        else:
            return json(Response(
                code=HttpCode.FAIL,
                message=str(error),
                data={}
            ))
