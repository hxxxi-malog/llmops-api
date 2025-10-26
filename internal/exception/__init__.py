"""
@Time : 2025/10/25 13:42
@Auth : maloghx@outlook.com
@File : __init__.py.py
"""

from .exception import (
    CustomException,
    FailException,
    ValidErrorException,
    NotFoundException,
    UnauthorizedException,
    ForbiddenException,
)

__all__ = [
    "CustomException",
    "FailException",
    "ValidErrorException",
    "NotFoundException",
    "UnauthorizedException",
    "ForbiddenException",
]
