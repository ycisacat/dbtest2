#coding=utf-8
from sina.temp import fans_and_follow as ff

__author__ = 'yc'
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","dbtest2.settings")
django.setup()

import uidcrawl as u
import writingtxt as wr
import multiprocessing as mul

if __name__=='__main__':
    uid=uni.getUser(1,2,1,2)
    pool = mul.Pool(processes=3)
    result = []
    result.append(pool.apply_async(u.getPage(uid,1,2)))
    result.append(pool.apply_async(ff.getFans(uid,1,2)))
    result.append(pool.apply_async(ff.getFollow(uid,1,2)))
    result.append(pool.apply_async(wr.tupling(uid,)))
    pool.close()
    pool.join()
    queue=q.get()
    # print queue
    w= wr.tupling(uid,queue[0],queue[1])
    s=wr.intodb(w)