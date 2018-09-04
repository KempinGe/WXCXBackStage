__author__ = 'HarricaneGe'

from Handles.BaseHandle import BaseHandler,StaticFileBaseHandler
from Tools.responceCode import RET
import logging
import json

class GoodsDetailHandler(BaseHandler):
    def post(self,*args, **kwargs):
        if self.json_args['goodsId']:
            sql =  'SELECT *  FROM xh_goods  LEFT JOIN xh_goods_detail ON  xh_goods.goodsId = xh_goods_detail.goodsId WHERE  xh_goods.goodsId =1'
            try:
                result = self.db.query(sql)[0]
            except Exception as e:
                logging.error(e)
                self.write(dict(code=RET.DBERR, errMessage="数据库查询失败"))
            if result :
                data = {}
                pArr = eval(result['goodsPropetys'])
                cDic = eval(result['goodsSubPropetys'])
                for i in range(0,len(pArr)):
                    pArr[i]['childsCurGoods'] = cDic[i]
                data['properties'] = pArr
                logging.debug(pArr)
                data['pics'] = eval(result['goodsDetailImages'])
                data['basicInfo'] = dict(pic = result['goodsSmallImg'],
                                         minPrice= result['goodsMinPrice'],
                                         numberOrders = result['numberOrders'],
                                         stores = result['goodsCount'],
                                         commissionType = 1 ,
                                         name = result['goodsName'],
                                         commission=10,
                                         numberGoodReputation = result['numberGoodReputation'])
                data['content'] = '<div style="text-align:center;"> ' + result['goodsContent'] + '  <br /><img src="http://www.xiexingcun.com/Poetry/6/images/53e.jpg" alt="" /><br /><img src="http://www.xiexingcun.com/Poetry/6/images/53.jpg" alt="" /><br /><br /><img src="http://www.xiexingcun.com/Poetry/6/images/53b.jpg" alt="" /><br /></div>'
                self.write(dict(code=RET.OK, data=data))
            else:
                self.write(dict(code=RET.PARAMERR, errMessage="参数错误"))
