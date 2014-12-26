# coding: utf8

from dunk.utils.db import database
from dunk.model.user import User

def check_user(username,password):

    try:
        '''
        data = User.get_user_name_passwd_dictionary()
        #data = database.query('select name,password from sys_user')
        print "user_list is",data

        for x in data:
            if username == x['name']:
                if password == x['password']:
                    return True
        return False
        '''
        data = User.get_user_by_name(username)
        if len(data):
            if password == data['password']:
                return True
        else:
            return False


    except Exception, e:
        raise
    finally:
        database.close()
        return False