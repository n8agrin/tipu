import tornado.web
import simplejson
import time
from pymongo import Connection, json_util

class IssuesController(tornado.web.RequestHandler):
    
    def get(self):
        issues = list(Connection().tipu.issues.find())
        # i = list(issues.find())
        # self.set_header('Content-Type', 'text/json')
        # self.write(simplejson.dumps(i, default=json_util.default))
        self.render("../views/issues/get.html", issues=issues)
        
    def post(self):
        Connection().tipu.issues.insert({
            "raw": self.get_argument('issue'),
            "created_at": time.time()
        })
        self.redirect('/')
        
