# 导入蓝图对象
from flask import session, redirect, render_template, current_app, jsonify, request, g, url_for
# 导入模型类
from flask_web import db
# 导入自定义的状态码
from flask_web.utils.response_code import RET
from flask_restful import Resource

from . import example_blue


class Index(Resource):

    def get(self, id):
        return {"GET欢迎用户": id}

    def post(self, id):
        return "这是post请求"
