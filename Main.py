

from urls import urls
from Settings import *
from tornado import ioloop ,httpserver,options
from tornado.web import Application
from tornado.options import options,define
import torndb


define("port",default=8008,type=int,help="")

class WXSCApplication(Application):
    """"""
    def __init__(self,*args,**kwargs):
        super(WXSCApplication,self).__init__(*args,**kwargs)
        self.db = torndb.Connection(**MYSQL_SETTINGS)


def main():
    options.logging = LOG_LEVAL
    options.log_file_prefix = LOG_FILE
    options.parse_command_line()
    app = WXSCApplication(urls,**(APP_SETTINGS))
    http_request = httpserver.HTTPServer(app)
    http_request.listen(options.port)
    ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()

