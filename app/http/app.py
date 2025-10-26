"""
@Time : 2025/10/25 19:40
@Auth : maloghx@outlook.com
@File : app.py
"""
import dotenv
from injector import Injector

from internal.config import Config
from internal.router import Router
from internal.server import Http

# load env
dotenv.load_dotenv()
injector = Injector()
conf = Config()

app = Http(__name__, conf=conf, router=injector.get(Router))

if __name__ == "__main__":
    app.run(debug=True)
