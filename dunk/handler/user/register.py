# coding=utf-8

from tornado.web import RequestHandler
from dunk.utils.template import st
from dunk.utils.decorators import render
from dunk.utils.db import database
from dunk.model.user import User

class RegisterHandler(RequestHandler):

    @render
    def get(self):
        return st("user/register.html")

    def post(self):
        register_name = self.get_argument('register_name')
        register_passwd = self.get_argument('register_password')
        repeat_passwd = self.get_argument('repeat_passwd')
        
        print register_name
        print register_passwd

        if register_passwd != repeat_passwd:
            print "don't match"
            self.write("twice password don't match ")
        else:
            try:
                if User.get_user_by_name(register_name):
                    ''' this user have been registed'''
                    self.write("user exist")
                else:
                    if User.add_user_by_name_passwd(register_name,register_passwd):
                        self.write("regster sucess.")
                    else:
                        self.write("Add error.")


            except:
                raise
            finally:
                database.close()

