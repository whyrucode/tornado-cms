# coding: utf8

from tornado.web import url
from dunk.handler.api import PingHandler
from dunk.handler.user.login import LoginHandler
from dunk.handler.user.register import RegisterHandler
from dunk.handler.user.home import  HomeHandler


ROUTE_MAP = [
    url(r"/api", PingHandler),
    url(r"/", LoginHandler),
    url(r"/user/register",RegisterHandler),
    url(r"/home", HomeHandler),
]
