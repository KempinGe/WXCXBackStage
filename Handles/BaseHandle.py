#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'HarricaneGe'

from tornado.web import RequestHandler

class BaseHandler(RequestHandler):

    def get_current_user(self):
        return self.get_secure_cookie("User_Name")

    def get(self):
        pass

    def post(self):
        pass