# coding: utf8
from dunk.utils.template import st
from dunk.utils.decorators import render
from dunk.model.article import Articler
from tornado.web import RequestHandler
import random
import uuid

class  PushArticleHandler(RequestHandler):

    @render
    def get(self):

        return st('user/push_article.html')

        #self.render('login.html',title='登录')

    def post(self):
        Add_article_node={}

        article_info = {}

        print len(str(uuid.uuid1()))

        Add_article_node['id'] = str(uuid.uuid1())

        Add_article_node['article_catlog1'] = self.get_argument('push_article_catlog1')

        Add_article_node['article_catlog2'] = self.get_argument('push_article_catlog2')

        Add_article_node['auther'] = self.get_argument('push_article_author')

        Add_article_node['title'] = self.get_argument('push_article_title')

        Add_article_node['text'] = self.get_argument('push_article_text')

        Add_article_node['info'] = self.get_argument('push_article_info')

        #print "add_node_is:",Add_article_node

        Articler.add_one_item(Add_article_node)

        if not Articler.check_article(Add_article_node):
            return self.write("不和谐帖")
        else:
            self.redirect('/home')

class  PullPushArticleHandler(RequestHandler):

    @render
    def get(self):
        accountname = "wangnima@gmail.com"

        #print type(Articler.get_list_by_account(accountname).article_list)

        print Articler.get_list_by_account(accountname).article_list

        self.write("this page prepay to display article_list.")

