# coding: utf8

from tornado.escape import json_encode
from tornado.web import RequestHandler

from dunk.utils.decorators import jsonize


class PingHandler(RequestHandler):
    @jsonize
    def get(self):
        self.write(json_encode({
            'r': 1,
            'msg': 'ack',
        }))
