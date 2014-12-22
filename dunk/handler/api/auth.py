# coding: utf8

from dunk.model.db import database

def check_user(username,password):

    try:
        data = database.query('select name,password from sys_user')
        for x in data:
            if username == x['username']:
                if password == x['password']:
                    return True
        return False
    except Exception, e:
        raise
    finally:
        database.close()


