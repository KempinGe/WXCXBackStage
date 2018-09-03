
__author__ = 'HarricaneGe'

from Handles.BaseHandle import BaseHandler,StaticFileBaseHandler
from Tools.responceCode import RET
import logging
from Settings import STATIC_PATH

''' <view style="font-size: 35rpx"> ￥ {{item.moneyMax}}元 </view>
               <view> {{item.name}} </view>
               <view> 满 {{item.moneyHreshold}} 元使用 </view>
               <view wx:if="{{item.dateEndType == 0}}"> {{item.dateEnd}} 前有效 </view>
               <view wx:if="{{item.dateEndType == 1}}"> 领取 {{item.dateEndDays}} 天内有效 </view>'''

class CouponHandler(BaseHandler):
    def post(self,*args, **kwargs):
        arr = [{'id': 1,'name':'优惠大礼包','moneyMax':10 , 'moneyHreshold': 100.0,'dateEndType':0,'dateEnd':'2018-09-01'},
               {'id': 5,'name':'优惠大礼包','moneyMax':20 ,'moneyHreshold': 255.0,'dateEndType':1,'dateEnd':'2018-12-01'},
               {'id': 1, 'name':'优惠大礼包','moneyMax':30 ,'moneyHreshold': 355.0,'dateEndType':1,'dateEnd':'2018-10-01'},
               {'id': 6, 'name':'优惠大礼包','moneyMax':80 ,'moneyHreshold': 888.0,'dateEndType':0,'dateEnd':'2018-06-01'},
               {'id': 5, 'name':'优惠大礼包','moneyMax':100 ,'moneyHreshold': 1000.0,'dateEndType':1,'dateEnd':'2018-09-10'}]
        self.write(dict(code=RET.OK, data=arr))