#!/usr/bin/env python
#coding=utf-8
'''
9.3进程池
'''

__author__ = 'yc'
import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE","dbtest2.settings")
django.setup()

from test_page import *
from class_mysql_uid import *
import multiprocessing as mul
from proxyIp import *

if __name__ =='__main__':
    # getProxyIpControl() #更新代理ip池,每日第一次运行时开启,之后可以注释掉

    db=Database()
    page_crawler =Page()
    uid=db.get_mysql_user(1000,1002)
    pool=mul.Pool(processes=2)
    for i in uid:
        run=[page_crawler.count(uid,i),page_crawler.getPage(i,1,2)]
        for func in run:
            pool.apply_async(func)
    pool.close()
    pool.join()
