from django.conf.urls import *
from . import views,testdb
 
urlpatterns = [
    url(r'hello/', views.hello),
    url(r'testdb/', testdb.testdb),
]