import tornado
from tornado.web import RequestHandler
from dunk.utils.template import st
from dunk.utils.decorators import render

class RegisterHander(RequestHandler):
    @tornado.web.authenticated
    @render

    def get(self):
        return st("user/register.html")

    def post(self):
        name = self._get_argument('login_name')
        passwd = self.get_argument('password')
        re_passwd = self.get_argument('re_password')
'''
        if passwd != re_passwd:
            self.write("set password wrong ")
        else:
            try:
                #database.execute('insert into tornadoDB.sys_user(user_id,name,password) values(%s,%s,%s)',uuid(),name,password)
                pass

            Exception e:
                raise
            finally:
                database.close()

         self.redirect('/home')
'''

