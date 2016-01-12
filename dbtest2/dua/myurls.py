#coding=utf-8
__author__ = 'yc'
from django.contrib import admin
from django.conf.urls import url,patterns
from dua.views import *
from django.views.generic.list import ListView
from dua.models import *

urlpatterns = [
    url(r'^login',login_page,name='login_page'),
    url(r'^register',register_page,name='register_page'),
    url(r'^logout',logout_page,name='logout_page'),
    url(r'^main_page',main_page,name='main_page'),
    url(r'^get_id',get_id,name='get_id'),
    url(r'^kaixin',kaixin,name='kaixin'),
    url(r'^kuaile',kuaile,name='kuaile'),
    url(r'^manyi',manyi,name='manyi'),
    url(r'^tonghen',tonghen,name='tonghen'),
    url(r'^jingya',jingya,name='jingya'),
    url(r'^wunai',wunai,name='wunai'),
    url(r'^nanguo',nanguo,name='nanguo'),
    url(r'^buman',buman,name='buman'),
]
