# coding=utf-8

import torndb
from tornado.options import define

from dunk.utils.tornadb2 import *


define('port',default=8888,help='run on the port',type=int)

database=torndb.Connection('localhost','tornadoDB',user='bird',password='db123456')

database2 = Connection('localhost','tornadoDB',user='bird',password='db123456')


