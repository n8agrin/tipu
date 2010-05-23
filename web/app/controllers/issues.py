import tornado.web
import simplejson
from pymongo import Connection, json_util

conn = Connection()
db = conn.tipu
issues = db.issues

class IssuesController(tornado.web.RequestHandler):
    
    def get(self):
        i = list(issues.find())
        self.set_header('Content-Type', 'text/json')
        self.write(simplejson.dumps(i, default=json_util.default))
        self.finish()
        
    def post(self):
        issues.insert(self.request.arguments)
        self.finish()
        
