"""
@Time : 2025/10/25 19:23
@Auth : maloghx@outlook.com
@File : app_handler.py
"""
import os
import uuid
from dataclasses import dataclass

from injector import inject
from openai import OpenAI

from internal.exception import FailException
from internal.schema.app_schema import CompletionReq
from internal.service.app_service import AppService
from pkg.response import success_json, valid_error_json, success_message

@inject
@dataclass
class AppHandler:
    """应用控制器"""
    app_service: AppService

    def create_app(self):
        """调用服务创建新的APP记录"""
        app = self.app_service.create_app()
        return success_message(f"应用已经成功创建，id为{app.id}")

    def get_app(self, id: uuid.UUID):
        app = self.app_service.get_app(id)
        return success_message(f"应用已经成功获取，名字是{app.name}")

    def update_app(self, id: uuid.UUID):
        app = self.app_service.update_app(id)
        return success_message(f"应用已经成功修改，修改的名字是:{app.name}")

    def delete_app(self, id: uuid.UUID):
        app = self.app_service.delete_app(id)
        # 可根据需求补充返回信息，例如返回删除成功的提示
        return success_message(f"应用已成功删除，id为{app.id}")

    def completion(self):
        """聊天接口"""
        req = CompletionReq()
        if not req.validate():
            return valid_error_json(req.errors)

        client = OpenAI(base_url=os.getenv("OPENAI_API_BASE"))

        completion = client.chat.completions.create(
            model="qwen3-max",
            messages=[
                {'role': 'system', 'content': '你是Malog开发的AI助手'},
                {'role': 'user', 'content': req.query.data}
            ]
        )

        content = completion.choices[0].message.content

        return success_json({"content": content})

    def ping(self):
        """服务器测试接口"""
        raise FailException("服务器测试接口")
        # return {"ping": "pong"}
