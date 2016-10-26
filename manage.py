#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app import create_app
from flask_script import Manager


#创建app实例
app=create_app()
manage=Manager(app)

if __name__=='__main__':
    manage.run()

