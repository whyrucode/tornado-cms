# coding: utf8

from dunk.api.dbapi import database

def check(username,password):

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