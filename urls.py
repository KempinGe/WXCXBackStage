#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'HarricaneGe'

from Handles.HomeHandle import MainHandler,GoodsList
from Handles.AuthenPageHandle import AuthenHandle
from tornado.web import StaticFileHandler

urls = [
	(r"/",MainHandler),
	(r"/Authen/a",AuthenHandle),
	(r"/Home/GoodsList",GoodsList),

	# (r'/.png',StaticFileHandler, dict(path=settings['static_path']))
	]