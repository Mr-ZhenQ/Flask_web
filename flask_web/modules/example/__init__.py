from flask import Blueprint
from flask_restful import Api

# 创建蓝图对象 # url_prefix="/example" 前缀
example_blue = Blueprint('example_blue', __name__)

docs = Api(example_blue)

# 把使用蓝图对象的文件导入到创建蓝图对象的下面
from . import views

# 绑定路由
docs.add_resource(views.Index, "/index/<int:id>")