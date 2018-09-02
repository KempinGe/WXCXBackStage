#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'HarricaneGe'

from tornado.web import RequestHandler
import json


class BaseHandler(RequestHandler):

    def prepare(self):
        """预解析json数据"""
        if self.request.headers.get("Content-Type", "").startswith("application/json"):
            self.json_args = json.loads(self.request.body)
        else:
            self.json_args = {}

    def get_current_user(self):
        return self.get_secure_cookie("User_Name")

    def get(self):
        pass

    def post(self):
        pass