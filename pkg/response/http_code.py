"""
@Time : 2025/10/26 10:55
@Auth : maloghx@outlook.com
@File : http_code.py
"""
from enum import Enum


class HttpCode(str, Enum):
    """HTTP 基础业务状态码"""

    SUCCESS = "success"  # 操作成功
    FAIL = "fail"  # 操作失败
    NOT_FOUND = "not_found"  # 资源未找到
    UNAUTHORIZED = "unauthorized"  # 未授权访问
    FORBIDDEN = "forbidden"  # 禁止访问
    VALID_ERROR = "valid_error"  # 验证错误
