"""
@Time : 2025/10/26 11:49
@Auth : maloghx@outlook.com
@File : exception.py
"""
from dataclasses import field
from typing import Any

from pkg.response import HttpCode


class CustomException(Exception):
    """自定义异常信息"""
    code: HttpCode = HttpCode.FAIL
    message: str = ""
    data: Any = field(default_factory=dict)

    def __init__(self, message: str = "", data: Any = None):
        super().__init__()
        self.message = message
        self.data = data


class FailException(CustomException):
    """失败异常"""
    pass


class NotFoundException(CustomException):
    """资源未找到异常"""
    code = HttpCode.NOT_FOUND


class UnauthorizedException(CustomException):
    """未授权异常"""
    code = HttpCode.UNAUTHORIZED


class ForbiddenException(CustomException):
    """禁止访问异常"""
    code = HttpCode.FORBIDDEN


class ValidErrorException(CustomException):
    """验证错误异常"""
    code = HttpCode.VALID_ERROR
