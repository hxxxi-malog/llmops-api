"""
@Time : 2025/10/26 12:20
@Auth : maloghx@outlook.com
@File : test_app_handler.py
"""
from pkg.response import HttpCode


class TestAppHandler:
    """app 控制器测试类"""

    def test_completion(self, client):
        """测试聊天接口"""
        resp = client.post("/app/completion", json={"query": "你好，你是谁？"})
        assert resp.status_code == 200
        assert resp.json.get("code") == HttpCode.SUCCESS
        print("响应内容: ", resp.json)