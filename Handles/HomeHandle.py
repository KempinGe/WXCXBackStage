from tornado.web import RequestHandler

class MainHandler(RequestHandler):

	def get(self):
		self.write('hello world')


	def post(self):
		self.write({'title':'python'})
