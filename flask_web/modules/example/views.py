# 导入蓝图对象
from flask import session, redirect, render_template, current_app, jsonify, request, g, url_for
# 导入模型类
from flask_web import db
# 导入自定义的状态码
from flask_web.utils.response_code import RET
from . import example_blue


# json渲染
@example_blue.route('/')
def index():
    return "Hello flask_web"


# 模板渲染
@example_blue.route('/templates')
def hello():
    data = {"data": "example"}
    return render_template('example/index.html', data=data)


# 路由过滤器+json渲染
@example_blue.route('/<int:id>')
def user(id):
    return jsonify({"欢迎用户": id})


# 重定向
@example_blue.route('/test')
def index_url_for():
    return redirect(url_for("example_blue.index"))
