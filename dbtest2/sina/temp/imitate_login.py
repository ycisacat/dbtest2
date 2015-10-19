# coding=utf-8
__author__ = 'gu'
import django, os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dbtest2.settings")
django.setup()

import time, random, urllib2, re, multiprocessing as mul, MySQLdb, cookielib, urllib, sys
from dua.models import *
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from _mysql_exceptions import ProgrammingError


class ImitateLogin:
    def __init__(self):
        self.base_dir = '/home/gu/dbtest2/sina/results/'
        self.text_dir = '/home/gu/dbtest2/sina/blogtext/'
        self.default_title = "anonymous"
        self.header = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:35.0) Gecko/20100101 Firefox/35'}
        # 'cookie':'SUHB=0auQu-VKohQewN; Hm_lvt_16374ac3e05d67d6deb7eae3487c2345=1438853337; gsid_CTandWM=4uNEa18a1iXLheOZzx4XAnLede5; _T_WM=9680670dc09c465d401000970f08a051'}
        # 'cookie':'SUB=_2A254_6A0DeTxGeNI7VER-S3EzD-IHXVYA8B8rDV6PUJbrdAKLUbekW1-zwbkLzaRdvZqxj6DUj5ImWtgBQ..; expires=Sun'
        # ', 18-Oct-2015 08:50:44 GMT; path=/; domain=.weibo.cn; httponly'
        # 'gsid_CTandWM=4uNEa18a1iXLheOZzx4XAnLede5; expires=Sun, 18-Oct-2015 08:50:44 GMT; path=/; domain=.weibo'
        # '.cn; httponly'
        # 'PHPSESSID=f9fda472d39c7edf93bae7a2cd950d7f; path=/'}
        self.user_list = []
        self.weibo_list = []
        self.time_list = []
        self.weibo = []
        self.writing_time = []
        self.fans_list = []
        self.gd_fans = []
        self.follow_list = []
        self.gd_follow = []
        self.cj = cookielib.LWPCookieJar()
        # if cookie_filename is not None:
        #     self.cj.load(cookie_filename)
        # 将一个保存cookie对象，和一个HTTP的cookie的处理器绑定
        self.cookie_processor = urllib2.HTTPCookieProcessor(self.cj)
        # 创建一个opener，将保存了cookie的http处理器，还有设置一个handler用于处理http的URL的打开
        self.opener = urllib2.build_opener(self.cookie_processor, urllib2.HTTPHandler)
        # 将包含了cookie、http处理器、http的handler的资源和urllib2对象绑定在一起
        urllib2.install_opener(self.opener)
        self.headers = {'User-Agent': 'Mozilla/' + str(
            float(int(random.uniform(1, 6)))) + '(X11; Ubuntu; Linux i686; rv:35.0) Gecko/20100101 Firefox/' + str(
            float(int(random.uniform(29, 36))))}
        self.account = [('nrrfdzpc@sina.cn', 'tttt5555'), ('zgryejmd@sina.cn', 'tttt5555'),
                        ('nowccqpq@sina.cn', 'tttt5555'),
                        ('odlmyfbw@sina.cn', 'tttt5555'), ('ajjqbwkm@sina.cn', 'tttt5555'),
                        ('xgakyvbj@sina.cn', 'tttt5555'),
                        ('coiarurd@sina.cn', 'tttt5555')]

    def database(self):
        conn = MySQLdb.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            passwd='uliuli520',
            db='sina',
            charset='utf8', )

        cur = conn.cursor()

        cur.execute('create table SinaUser'
                    '(user_id varchar (20),user_name varchar (20) primary key )'
                    'ENGINE=MyISAM DEFAULT CHARSET=utf8;')
        cur.execute('create table GDFollow'
                    '(user_id varchar (20) not null,gdfollows_id varchar (20) not null ,'
                    'primary key(user_id ,gdfollows_id) )'
                    'ENGINE=MyISAM DEFAULT CHARSET=utf8;')
        cur.execute('create table GDFans'
                    '(user_id varchar (20) not null,gdfans_id varchar (20) not null,primary key(user_id,gdfans_id) )'
                    'ENGINE=MyISAM DEFAULT CHARSET=utf8;')
        cur.execute('create table MyUser'
                    '(name varchar (20),password varchar (20))'
                    'ENGINE=MyISAM DEFAULT CHARSET=utf8;')
        cur.close()
        conn.commit()
        conn.close()



