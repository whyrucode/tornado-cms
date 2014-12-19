# coding: utf8

from tornado.web import Application
from tornado.ioloop import IOLoop

from dunk.route import ROUTE_MAP


def make_app():
    return Application(ROUTE_MAP)


if __name__ == '__main__':
    app = make_app()
    app.listen(8888)
    IOLoop.current().start()
