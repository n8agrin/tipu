import tornado.web

class HelloController(tornado.web.RequestHandler):
    
    def get(self):
        self.finish("Hello!")
