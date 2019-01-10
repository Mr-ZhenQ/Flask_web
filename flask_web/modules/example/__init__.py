from flask import Blueprint

# 创建蓝图对象 # url_prefix="/example" 前缀
example_blue = Blueprint('example_blue', __name__)

# 把使用蓝图对象的文件导入到创建蓝图对象的下面
from . import views
