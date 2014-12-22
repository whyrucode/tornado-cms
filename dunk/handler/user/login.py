# coding: utf8

from tornado.web import RequestHandler
from dunk.utils.template import st
from dunk.utils.decorators import render
from dunk.handler.api.auth import check_user


class LoginHandler(RequestHandler):

    @render
    def get(self):
        return st('user/login.html',message='登陆')

    def post(self):
         name = self._get_argument('login_name')
         passwd = self.get_argument('password')

         if not check_user(name,passwd):
             return self.write("账户名或者密码错误！")

         self.set_secure_cookie('usr',name)
         self.redirect('/home')





