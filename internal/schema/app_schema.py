"""
@Time : 2025/10/25 22:12
@Auth : maloghx@outlook.com
@File : app_schema.py
"""
from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField
from wtforms.validators import DataRequired, Length


class CompletionReq(FlaskForm):
    """基础聊天请求验证"""
    query = StringField("query", validators=[
        DataRequired(message="用户的提问是必填"),
        Length(max=2000, message="用户的最大提问长度是2000")
    ])