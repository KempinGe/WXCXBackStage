__author__ = 'HarricaneGe'

from Handles.BaseHandle import BaseHandler,StaticFileBaseHandler
from Tools.responceCode import RET
import logging


class GoodsDetailHandler(BaseHandler):
    def post(self,*args, **kwargs):
        data = {"properties":[{"idx":'idx',"name":'propertie1',"id":0,"childsCurGoods":[{"name":'childsCurGoods',"id":999}]}],"selectSize":1,
                "basicInfo" :{"minPrice":10,"minScore":20,"stores":9999,"numberGoodReputation":100,"numberOrders":200,"commissionType":1,
                              "commission" : "10","name":"这个是商品名称吗"
                              },
                "content" :'<div style="text-align:center;">《静夜思》· 李白<br />床前明月光，<br />疑是地上霜。 <br />举头望明月， <br />低头思故乡。<br /><img src="http://www.xiexingcun.com/Poetry/6/images/53e.jpg" alt="" /><br /><img src="http://www.xiexingcun.com/Poetry/6/images/53.jpg" alt="" /><br /><br /><img src="http://www.xiexingcun.com/Poetry/6/images/53b.jpg" alt="" /><br /></div>'}
        # "videoId": "什么是videoId"
        self.write(dict(code=RET.OK, data=data))