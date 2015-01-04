__author__ = 'BIRDS'

from dunk.utils.template import st
from dunk.utils.decorators import render
from dunk.model.article import Articler
from tornado.web import RequestHandler

class  ArticleHandlerlist(RequestHandler):

    @render
    def get(self):
        '''
        accountname = "wangnima@gmail.com"

        #print type(Articler.get_list_by_account(accountname).article_list)

        print Articler.get_list_by_account(accountname).article_list

        self.write("this page prepay to display article_list.")
        '''
        return st('ueditor/ueditor.html')