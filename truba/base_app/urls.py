#coding:utf8
from django.conf.urls import url
from django.contrib import admin
from views import *

urlpatterns = [
    url(r'^base/', grand),
    
    url(r'c=(?P<catalog_resp>[^/]+)/$',choise_catalog),
    url(r'p=(?P<prod_resp>[^/]+)/$',choise_production),
    url(r'^order/$',add_order),
    url(r'^$', grand),

]
