#coding:utf-8

from django.db import models
from mongoengine import *

#。db里面的表的命名的方式为：类_表名。例如：WebServer_Template_1，下方只填写表名。
# ID为主键，不需要定义； name 类型为字符串，长度为30，值为唯一 ； selected为布尔值。

class Test(Document):
    name = StringField(max_length=200)
    meta = {'allow_inheritance': True} ##允许后续增加字段
