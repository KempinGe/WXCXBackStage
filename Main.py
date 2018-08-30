

from urls import urls
from tornado.web import RequestHandler, Application
from tornado.ioloop import IOLoop

print(__file__)

if __name__ == "__main__":
    application = Application(urls)
    application.listen(8888)
    IOLoop.current().start()

