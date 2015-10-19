#coding=utf-8
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","dbtest2.settings")
django.setup()

from sina.class_all_id import Sina


if __name__=='__main__':          #因为多线程会比单线程慢,所以改为用多进程了
    crawler = Sina()
    uid=crawler.getUser(1,2,1,2)
    for i in uid:
        fans=crawler.getFans(i,1,2)
        follow=crawler.getFollow(i,1,2)
        blog=crawler.getPage(i,1,2)



