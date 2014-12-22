# coding=utf-8

import torndb
from tornado.options import define,options,parse_command_line 


define('port',default=8888,help='run on the port',type=int)  
 
database=torndb.Connection('localhost','tornadoDB',user='bird',password='db123456')
