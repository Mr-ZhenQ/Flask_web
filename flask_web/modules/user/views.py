# 导入蓝图对象
from flask import session, redirect, render_template, current_app, jsonify, request, g, url_for
# 导入模型类
from flask_web import db
# 导入自定义的状态码
from flask_web.utils.response_code import RET
from . import user_blue


# json渲染
@user_blue.route('/')
def index():
    return "Hello World"


# 模板渲染
@user_blue.route('/templates')
def hello():
    data = {"v": "m"}
    return render_template('user/index.html', data=data)


# 路由过滤器+json渲染
@user_blue.route('<int:id>')
def user(id):
    return jsonify({"欢迎用户": id})


# 重定向
@user_blue.route('/test')
def index_url_for():
    return redirect(url_for("user_blue.index"))
