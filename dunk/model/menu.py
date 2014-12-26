# coding: utf8
from dunk.utils.db import database

class Menu(object):

    def __init__(self, parents_id,m_id, name,url):

        self.parents_id = parents_id
        self.m_id = m_id
        self.menu_name = name
        self.url = url

    @classmethod
    def get_by_name(self,user_name):
        res = database.query("select p_menu_id, menu_id,name from business_menu where name=%s" % user_name)
        if len(res) != 1:
            return None
        return Menu(res[0]['p_menu_id'], res[0]['menu_id'],res[0]['name'],res[0]['url'] )

    @classmethod
    def add_item(self,MenuNode):

        _table_name ="biz_menu"

        result = database.execute('insert into _table_name(id,p_menu_id,menu_id,name,url) values(UUID(),"%s,"%s,"%s","%s")'%(MenuNode['p_menu_id'],MenuNode['menu_id'],MenuNode['name'],MenuNode['url']))

        if len(result) < 1:
            return False
        return True

