#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from werkzeug.utils import import_string
from flask_sqlalchemy import SQLAlchemy
import os

db=SQLAlchemy()
bluepoints=[
    ('app.views.zen.main_page:main',None)
]
def create_app():
    """
    创建应用
    :return:
    """
    app=Flask(__name__)
    #配置app
    load_config(app)
    load_blueprints(app)
    db.init_app(app)
    return app

def load_config(app):
    """
    根据uwsgi文件加载对应的环境
    :param app:
    :return:
    """
    app.config.from_object('config.ProductConfig') if os.environ.get('ZEN_ENV','dev')=='prod' else app.config.from_object('config.DevelopConfig')

def load_blueprints(app):
    for bp_info in bluepoints:
        bp=import_string(bp_info[0])
        app.register_blueprint(bp,url_prefix=bp_info[1])
