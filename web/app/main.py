import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado.options import define, options

# Controllers
from controllers.issues import IssuesController

application = tornado.web.Application([
    (r"/", IssuesController),
])

if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
