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

from class_page import *
import multiprocessing as mul,json


if __name__ =='__main__':
    page_crawler =Page()
    uid=page_crawler.download()
    print uid
    pool=mul.Pool(processes=5)
    for i in uid:
        run=[page_crawler.getPage(uid,1,2)]
        for func in run:
            pool.apply_async(func)
    pool.close()
    pool.join()
