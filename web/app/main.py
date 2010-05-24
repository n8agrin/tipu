import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado.options import define, options

# App options
define("port", default=8888, help="web server port", type=int)
define("debug", default=False, help="debug mode, will force re-compilation of templates and auto-reload of True", type=bool)

# Controllers
from controllers.issues import IssuesController

application = tornado.web.Application([
    (r"/", IssuesController),
])

if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
