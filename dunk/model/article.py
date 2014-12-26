# coding: utf8
from dunk.utils.db import database
from dunk.utils.db import database2

class Articler(object):

    def __init__(self, article_list):
        self.article_list = article_list

    @classmethod
    def get_list_by_account(self,article_auther):

        res = database.query('select * from biz_ariticle where auther = "%s"'%article_auther)

        #print "get_by_account res",res

        if len(res) < 1:
            return None
        return Articler(res)

    @classmethod
    def add_one_item(self,Add_Node):
        _table_name ="biz_ariticle"
        #Add_Node['auther'],Add_Node['catlog1'],Add_Node['catlog2'],Add_Node['text'],Add_Node['info'])
        print type(Add_Node)
        print Add_Node
        database2.insert_by_dict(_table_name,Add_Node)

    @classmethod
    def check_article(self,Add_Node):
        return  True


