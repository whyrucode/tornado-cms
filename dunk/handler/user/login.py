# coding: utf8

from tornado.web import RequestHandler
from dunk.utils.template import st
from dunk.utils.decorators import render
from dunk.model.user import User


class LoginHandler(RequestHandler):

    @render
    def get(self):
        return st('user/login.html')
        #self.render('login.html',title='登录')

    def post(self):
         name = self.get_argument('login')
         passwd = self.get_argument('password')

         print "logn_name",name
         print "password",passwd

         user = User.get_user_by_name_and_password(name, passwd)
    
         if not user:
             return self.write("账户名或者密码错误！")

         #self.set_secure_cookie('usr',name)
         self.redirect('/home')





