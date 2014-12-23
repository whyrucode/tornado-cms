#coding=utf-8
from tornado.web import RequestHandler
from dunk.utils.template import st
from dunk.utils.decorators import render
from dunk.utils.db import database

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
                #判定是否存在
                result_list = database.query('select name from sys_user where name="%s"'%register_name)
                print "user_is_exisit",len(result_list),result_list
                
                if len(result_list):
                    ''' this user have been registed'''
                    self.write("user exist")

                else:
                    #insert mysql
                    result = database.execute('insert into tornadoDB.sys_user(name,password) values("%s","%s")'%(register_name,register_passwd))
                    self.write("regster sucess !")

            except:
                raise
            finally:
                database.close()
                #self.redirect('/home')

