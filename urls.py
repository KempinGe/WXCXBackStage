#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'HarricaneGe'

from Handles.HomeHandle import *
from Handles.CouponHandlers import *
from Handles.GoodsHandlers import *
from Handles.AuthenPageHandle import AuthenHandle
from tornado.web import StaticFileHandler

urls = [
	(r"/",MainHandler),
	(r"/Authen/a",AuthenHandle),
	(r"/Home/BannerList", BannerListHandler),
	(r"/Home/GoodsList",GoodsListHandler),
	(r"/Home/CotegoriList",CategorieListHandler),
    (r"/Home/CouponList",CouponHandler),
    (r"/Home/NoticeList",NoticeListHandler),
    (r"/Goods/Detai",GoodsDetailHandler)
	# (r'/.png',StaticFileHandler, dict(path=settings['static_path']))
	]