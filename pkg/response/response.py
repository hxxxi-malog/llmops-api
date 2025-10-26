"""
@Time : 2025/10/26 11:01
@Auth : maloghx@outlook.com
@File : response.py
"""
from flask import jsonify

from .http_code import HttpCode
from typing import Any
from dataclasses import field, dataclass


@dataclass
class Response:
    """基础 HTTP 接口响应格式"""

    code: HttpCode = HttpCode.SUCCESS
    message: str = ""
    data: Any = field(default_factory=dict)


def json(data: Response = None):
    """基础消息响应"""
    return jsonify(data), 200


def success_json(data: Any = None):
    """成功消息响应"""
    return json(Response(code=HttpCode.SUCCESS, message="", data=data))


def fail_json(message: str, data: Any = None):
    """失败消息响应"""
    return json(Response(code=HttpCode.FAIL, message=message, data=data))


def valid_error_json(errors: dict = None):
    """验证错误消息响应"""
    first_key = next(iter(errors))
    if first_key is not None:
        msg = errors.get(first_key)[0]
    else:
        msg = ""
    return json(Response(code=HttpCode.VALID_ERROR, message=msg, data=errors))


def message(code: HttpCode, msg: str = ""):
    """基础响应消息，返回固定消息，数据固定字典为空"""
    return json(Response(code=code, message=msg, data={}))


def success_message(msg: str = ""):
    """成功消息"""
    return message(HttpCode.SUCCESS, msg=msg)


def fail_message(msg: str = ""):
    """失败消息"""
    return message(HttpCode.FAIL, msg=msg)


def not_found_message(msg: str = ""):
    """资源未找到消息"""
    return message(HttpCode.NOT_FOUND, msg=msg)


def unauthorized_message(msg: str = ""):
    """未授权消息"""
    return message(HttpCode.UNAUTHORIZED, msg=msg)


def forbidden_message(msg: str = ""):
    """禁止访问消息"""
    return message(HttpCode.FORBIDDEN, msg=msg)
