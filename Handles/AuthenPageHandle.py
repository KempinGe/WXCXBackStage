#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'HarricaneGe'

from Handles.BaseHandle import BaseHandler

class AuthenHandle(BaseHandler):
    def get(self):

        if self.current_user :
            self.redirect('/', permanent=True)
        self.write('<html><body><form action="/Authen/a" method="post">'
                    '<input type="text" name="message">'
                    '<hr/>'
                    '<input type="submit" value="请输入姓名">'
                    '</form></body></html>')

    def post(self):
        self.set_secure_cookie('User_Name',self.get_argument('message'))
        self.redirect('/', permanent=True)