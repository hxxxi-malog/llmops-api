"""
@Time : 2025/10/25 19:23
@Auth : maloghx@outlook.com
@File : app_handler.py
"""
import uuid
from dataclasses import dataclass

from injector import inject
from uuid import UUID
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

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

    def debug(self, app_id: UUID):
        """聊天接口"""

        # 创建请求对象并验证参数
        req = CompletionReq()
        if not req.validate():
            return valid_error_json(req.errors)

        system = """
        你是由Malog开发的AI人工智能助手，热心回答一切知道的问题。
        """

        # 创建聊天提示模板，使用系统提示词和用户查询
        prompt = ChatPromptTemplate.from_messages([
            ("system", system),
            ("user", "{query}")
        ])
        # 初始化ChatOpenAI模型，指定使用qwen3-max模型
        llm = ChatOpenAI(model="qwen3-max")
        # 创建字符串输出解析器，用于解析模型输出
        parser = StrOutputParser()

        # 构建处理链：提示模板 -> LLM模型 -> 输出解析器
        chain = prompt | llm | parser

        # 执行链式调用，传入查询数据并获取处理结果
        content = chain.invoke({"query": req.query.data})

        # 返回成功响应
        return success_json({"content": content})

    def ping(self):
        """服务器测试接口"""
        raise FailException("服务器测试接口")
        # return {"ping": "pong"}
