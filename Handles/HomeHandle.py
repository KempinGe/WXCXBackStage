#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'HarricaneGe'

from tornado.web import RequestHandler
from Handles.BaseHandle import BaseHandler


class GoodsList(BaseHandler):
	def get(self):
		self.write('hellow world')

	def post(self):
		pass



class MainHandler(BaseHandler):
	def get(self):
		if self.current_user:
			self.write('<html><body><form action="/" method="post">'
						'<input type="text" name="message" ,value = "你好">'
					   '<input type="submit" value="查看INFO" >'
					   '</form></body></html>')
		else:
			self.write('<html><body><form action="/" method="post">'
					   '<input type="text" name="message">'
					   '<input type="submit" value="清除cookie" >'
					   '</form></body></html>')
	def post(self):
		if self.current_user:
			msg = self.get_argument('message')
			self.write({'title': msg,'name':self.current_user.decode("utf-8")})
		else:
			self.write('请登录')

