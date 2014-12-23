# coding: utf8

from tornado.web import RequestHandler
from dunk.utils.decorators import render
from dunk.utils.template import st

class HomeHandler(RequestHandler):

    @render
    def get(self):
        return st('index.html')

    def post(self):
        pass

