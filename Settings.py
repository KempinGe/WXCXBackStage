#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'HarricaneGe'

import os


LOG_LEVAL = 'debug'
STATIC_PATH = os.path.join(os.path.dirname(__file__),'Assets')
LOG_FILE = os.path.join(os.path.dirname(__file__),'logs/logs.logs')


APP_SETTINGS = {
    "static_path": STATIC_PATH,
    'debug' : True,
    "cookie_secret": "PQvw9USaSwWuPNrs6m6x/MsurHFz6UjGrqOXeK4GAoU=",
    "xsrf_cookies": True,
}

#数据库设置
MYSQL_SETTINGS=dict(
    database='WXSCDATABASE',
    host='127.0.0.1',
    user='root',
    password='g123567G'
)


CONFUSE = 'XBXKempinGe'