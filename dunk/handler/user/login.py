# coding: utf8

from tornado.web import RequestHandler
from dunk.utils.template import st
from dunk.utils.decorators import render


class LoginHandler(RequestHandler):
    @render
    def get(self):
        return st('user/login.html')
