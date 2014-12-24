# coding: utf8

from dunk.utils.db import database


class User(object):

    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

    @classmethod
    def get(self, user_id):
        res = database.query("select user_id, name from sys_user where user_id=%s" % user_id)
        if len(res) != 1:
            return None
        return User(res[0]['user_id'], res[0]['name'])

    @classmethod
    def get_user_by_name(self, name):
        res = database.query("select user_id from sys_user where name='%s'" % name)
        return User.get(res[0]['user_id']) if res else None

    @classmethod
    def add_user_by_name_passwd(self,name,password):
        result = database.execute('insert into tornadoDB.sys_user(name,password) values("%s","%s")'%(name,password))
        print "add_user_by_name_passwd:",result
        if result > 0 :
            return True
        else:
            return False

    @classmethod
    def get_user_name_passwd_dictionary(self):
        UserList = []
        UserList = database.query('select name,password from sys_user')
        
        return UserList


