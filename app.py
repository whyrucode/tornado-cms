# coding: utf8
import os
from tornado.web import Application,StaticFileHandler
from tornado.ioloop import IOLoop
from dunk.route import ROUTE_MAP

def make_app():
    
    settings = {
        'debug': True,
        #'static_path': os.path.join( os.path.dirname(__file__), "static" ),
        #'template_path': os.path.join( os.path.dirname(__file__), "/dunk/templates" ),
        'cookie_secret': 'bZJc2sWbQLKos6GkHn/VB9oXwQt8S0R0kRvJ5/xJ89E=',
        'login_url': '/user/login'
        #'log_function':r'/var/log/httpd.log'
    }
    URL_MAP = ROUTE_MAP + [
         (r'/statics/(.*)', StaticFileHandler, {"path": "./statics"})
    ]

    return Application(URL_MAP, **settings)



if __name__ == '__main__':
    app = make_app()
    app.listen(8888)
    IOLoop.current().start()
