"""
@Time : 2025/10/25 19:23
@Auth : maloghx@outlook.com
@File : app_handler.py
"""
import os

from openai import OpenAI

from internal.schema.app_schema import CompletionReq
from pkg.response import success_json, valid_error_json


class AppHandler:
    """应用控制器"""

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
        return {"ping": "pong"}
