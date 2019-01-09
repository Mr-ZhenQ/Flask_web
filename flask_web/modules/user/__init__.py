from flask import Blueprint

# 创建蓝图对象
user_blue = Blueprint('user_blue', __name__, url_prefix="/user")

# 把使用蓝图对象的文件导入到创建蓝图对象的下面
from . import views
