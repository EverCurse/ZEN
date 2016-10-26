#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Blueprint,jsonify
from app.models.zen import Zen
main=Blueprint('main',__name__)

@main.route('/')
def main_page():
    res=Zen.query.all()
    rst=[]
    data={}
    for i in res:
        print i
        data['ip']=i.host
        data['listen_port']=i.listen_port
        rst.append(data)
    return jsonify(rst)