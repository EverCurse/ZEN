#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app import db

class Zen(db.Model):
    __tablename__='zen'
    id=db.Column(db.Integer(),primary_key=True,index=True)
    user=db.Column(db.String(128))
    passwd = db.Column(db.String(128))
    host=db.Column(db.String(32),nullable=False)
    listen_port=db.Column(db.String(32),nullable=False)
    conf_path=db.Column(db.String(256),nullable=False)
    extra=db.Column(db.String(512),nullable=True)

    def __repr__(self):
        return '<Zen %r>' % self.host


class Users(db.Model):
    __tablename__='users'
    id = db.Column(db.Integer(), primary_key=True, index=True)
    username=db.Column(db.String(128))
    passwd=db.Column(db.String(128))
    is_actived=db.Column(db.Integer())
    last_login=db.Column(db.Integer())
    role=db.Column(db.Integer())

    def __repr__(self):
        return '<Users %r>' % self.username