# -*- coding: utf-8 -*-
 
from django.http import HttpResponse
from mongoengine import *
from django.contrib.auth.decorators import login_required
 
from . models import Test
#from . import models

# 连接数据库
connect('wes_wgs', host='10.100.6.7', port=27017,username='wuser', password='berry2012')
def testdb(request):
	# 修改其中一个id=1的name字段，再save，相当于SQL中的UPDATE
	#test1 = Test.objects.get(name='bbbb')
	list =  Test.objects.all()
	#for item in list:
	#	print(type(item.name))
	test1 = Test.objects.get(name='cccc')
	test1.delete()
	#test1.name = 'Google'
	#test1.save()
	
	# 另外一种方式
	#Test.objects.filter(id=1).update(name='Google')
	
	# 修改所有的列
	# Test.objects.all().update(name='Google')
	
	return HttpResponse("<p>删除成功</p>")