#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'HarricaneGe'

from tornado.web import RequestHandler,StaticFileHandler

import json


class BaseHandler(RequestHandler):

    @property
    def db(self):
        return self.application.db

    def prepare(self):
        """预解析json数据"""
        if self.request.headers.get("Content-Type", "").startswith("application/json"):
            self.json_args = json.loads(self.request.body)
        else:
            self.json_args = {}

    def write_error(self, status_code, **kwargs):
        pass

    def get_current_user(self):
        return self.get_secure_cookie("User_Name")

    def get(self):
        pass

    def post(self):
        pass


class StaticFileBaseHandler(StaticFileHandler):
    """自定义静态文件处理类, 在用户获取html页面的时候设置_xsrf的cookie"""
    def __init__(self, *args, **kwargs):
        super(StaticFileBaseHandler, self).__init__(*args, **kwargs)

    # def prepare(self):
    #     """预解析json数据"""
    #     if self.request.headers.get("Content-Type", "").startswith("application/json"):
    #         self.json_args = json.loads(self.request.body)
    #     else:
    #         self.json_args = {}
