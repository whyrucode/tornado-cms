# coding: utf8

import six
from functools import wraps


def jsonize(func):
    @wraps(func)
    def _(self, *args, **kw):
        self.set_header('Content-Type', 'application/json')
        return func(self, *args, **kw)
    return _


def render(func):
    @wraps(func)
    def _(self, *args, **kw):
        r = func(self, *args, **kw)
        if isinstance(r, six.string_types):
            self.write(r)
    return _
