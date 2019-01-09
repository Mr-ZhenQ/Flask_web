# 导入的日志模块和日志处理模块
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask, session
# 导入扩展flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy
# 导入扩展flask_session，用来指定session信息存储的位置
from flask_session import Session
# 导入配置文件中的字典
from config import config, Config
# 导入redis
from redis import StrictRedis
# 导入扩展wtf
from flask_wtf import CSRFProtect, csrf

# 实例化sqlalchemy对象
db = SQLAlchemy()
# 实例化redis数据库对象，用来存储和业务逻辑相关的数据，比如图片验证码,decode_response把redis数据类型转成str
redis_store = StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT, decode_responses=True)

# 设置日志的记录等级
logging.basicConfig(level=logging.DEBUG)  # 调试debug级
# 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024 * 1024 * 10, backupCount=10)
# 创建日志记录的格式 日志等级 输入日志信息的文件名 行数 日志信息
formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
# 为刚创建的日志记录器设置日志记录格式
file_log_handler.setFormatter(formatter)
# 为全局的日志工具对象（flask app使用的）添加日志记录器,current_app用来记录项目日志；
logging.getLogger().addHandler(file_log_handler)


# 工厂函数：可以让函数根据传入的参数的不同，生产不同的app
def create_app(config_name):
    app = Flask(__name__)
    # 使用配置信息
    app.config.from_object(config[config_name])

    # 实例化Session对象
    Session(app)
    # 通过init_app方法,让db和app进行关联
    db.init_app(app)

    # 使用wtf扩展实现csrf保护
    CSRFProtect(app)

    # 使用请求钩子，在每次请求后，写入到客户端浏览器的cookie中，写入csrf_token
    @app.after_request
    def after_request(response):
        csrf_token = csrf.generate_csrf()
        response.set_cookie('csrf_token', csrf_token)
        return response

    # 导入蓝图对象，注册蓝图
    from flask_web.modules.user import user_blue
    app.register_blueprint(user_blue)

    # TODO 导入蓝图 && 注册蓝图

    # 返回app
    return app
