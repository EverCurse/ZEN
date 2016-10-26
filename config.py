#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Config(object):
    pass


class ProductConfig(Config):
    pass

class DevelopConfig(Config):
    # 数据库配置
    DATABASE = {
        'host': 'localhost',
        'port': 3306,
        'user': 'docker',
        'passwd': 'docker',
        'db': 'zen'
    }
    DEBUG=True
    # Flask-Sqlalchemy 配置
    SQLALCHEMY_DATABASE_URI = 'mysql://{user}:{passwd}@{host}:{port}/{db}'.format(**DATABASE)
    #如果设置成 True，SQLAlchemy 将会记录所有 发到标准输出(stderr)的语句，这对调试很有帮助。
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True