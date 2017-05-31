# -*- coding: utf8 -*-
from flask import Blueprint
# 创建蓝本以定义路由
# 程序的路由保存在包里的app/main/views.py 模块中，而错误处理程序保存在app/main/
# errors.py 模块中。导入这两个模块就能把路由和错误处理程序与蓝本关联起来
main = Blueprint('main', __name__)
from . import views, errors