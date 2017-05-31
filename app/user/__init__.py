# -*- coding: utf8 -*-
"""
auth是有关用户认证的
"""
from flask import Blueprint

user = Blueprint('user',__name__)

from . import views