# coding: utf8

from tornado.web import url
from dunk.handler.api import PingHandler
from dunk.handler.user.login import LoginHandler
from dunk.handler.user.register import RegisterHandler
from dunk.handler.user.home import  HomeHandler
from dunk.handler.user.del_article import *

ROUTE_MAP = [
    url(r"/api", PingHandler),
    url(r"/", LoginHandler),
    url(r"/user/login", LoginHandler),
    url(r"/user/register", RegisterHandler),
    url(r"/home", HomeHandler),
    url(r"/user/pull_article", PullPushArticleHandler),
    url(r"/user/push_article", PushArticleHandler),
]
