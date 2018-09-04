#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'HarricaneGe'

from Handles.BaseHandle import BaseHandler,StaticFileBaseHandler
from Tools.responceCode import RET
import logging
from Settings import STATIC_PATH


class BannerListHandler(BaseHandler):
    def post(self,*args, **kwargs):
        arr = [{'Id': 1 , 'picUrl':  '/images/Banner/banner1.jpg'},
               {'Id': 5 , 'picUrl' : '/images/Banner/banner2.jpg'},
               {'Id': 1 , 'picUrl' : '/images/Banner/banner3.jpg'},
               {'Id': 6 , 'picUrl' : '/images/Banner/banner4.jpg'},
               {'Id': 5 , 'picUrl' : '/images/Banner/banner5.jpg'}]
        self.write(dict(code=RET.OK, data=arr))


class CategorieListHandler(BaseHandler):
	def post(self,*args, **kwargs):
		arr = [{'id': 1 ,'name':'分类一', 'activeCategoryId': 1},
               {'id': 2 ,'name':'分类二', 'activeCategoryId': 5},
               {'id': 3 ,'name':'分类三', 'activeCategoryId': 1},
               {'id': 4 ,'name':'分类四', 'activeCategoryId': 6},
               {'id': 5 ,'name':'分类五', 'activeCategoryId': 5}]
		self.write(dict(code=RET.OK, data=arr))



class GoodsListHandler(BaseHandler):
    def post(self,*args, **kwargs):
        sql = 'SELECT goodsId,goodsName,goodsSmallImg,goodsMinPrice,goodsOriginPrice FROM xh_goods'
        try:
            result = self.db.query(sql)
        except Exception as e:
            logging.error(e)
            self.write(dict(code=RET.DBERR, errMessage="数据库查询失败"))
        self.write(dict(code=RET.OK, data=result))  



class NoticeListHandler(BaseHandler):
    def post(self,*args, **kwargs):
        arr = {'dataList':[{ 'id':1,'title': "通知(0)(1)"},
                           {'id': 2, 'title': "通知(0)(2)"},
                           {'id': 3, 'title': "通知(0)(3)"},
                           ]}


        self.write(dict(code=RET.OK, data=arr))


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

