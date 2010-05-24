import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado.options import define, options
import os

# App options
define("port", default=8888, help="web server port", type=int)
define("debug", default=False, help="debug mode, will force re-compilation of templates and auto-reload of True", type=bool)

# Controllers
from controllers.issues import IssuesController
from controllers.hello import HelloController

# Application 
class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            tornado.web.url(r"/", IssuesController, name="front"),
            tornado.web.url(r"/hello", HelloController, name="hello"),
        ]
        settings = dict(
            cookie_secret="e220cf903f537500f6cfcaccd64df14d",
            debug=options.debug,
            static_path=os.path.join(os.path.dirname(__file__), "public"),
            template_path=os.path.join(os.path.dirname(__file__), "views"),
            xsrf_cookies=True,
        )
        #self.someapplicationlevelproperty = "bar"
        tornado.web.Application.__init__(self, handlers, **settings)

# Init
if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
