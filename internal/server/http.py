"""
@Time : 2025/10/25 19:37
@Auth : maloghx@outlook.com
@File : http.py
"""
from flask import Flask

from internal.config import Config
from internal.router import Router


class Http(Flask):
    """Http 服务引擎"""

    def __init__(self, *args, conf: Config, router: Router, **kwargs):
        super().__init__(*args, **kwargs)
        # 注册应用录路由
        router.register_router(self)

        self.config.from_object(conf)
