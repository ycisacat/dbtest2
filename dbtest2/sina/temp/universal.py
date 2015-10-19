#coding=utf-8
__author__ = 'gu'

import time
import random
import urllib2
import re
import functools
import httplib

from django.core.exceptions import ObjectDoesNotExist

from dua.models import *
import sina.temp.ip_changing as ipc


class BoundHTTPHandler(urllib2.HTTPHandler):
    def __init__(self, source_address=None, debuglevel=0):
        urllib2.HTTPHandler.__init__(self, debuglevel)
        self.http_class = functools.partial(httplib.HTTPConnection,
                source_address=source_address)

    def http_open(self, req):
        return self.do_open(self.http_class, req)

handler = BoundHTTPHandler(source_address=("192.168.1.10", 0))
opener = urllib2.build_opener(handler)
urllib2.install_opener(opener)

def ip_changing():
    bindIpObj= ipc.BindIp()
    bindIpObj. randomIp() #随机切换IP
    a=bindIpObj.getIp() #得到当前IP
    bindIpObj. changeIp(a)

def header():
    Header = {
    'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0',
    # res=Wed, 09-Sep-2015 14:06:23 GMT; path=/; domain=.weibo.cn; httponly gsid_CTandWM=4uUpd98d1Y19xdffKHLI1nNMWfH; expires=Wed, 09-Sep-2015 14:06:23 GMT; path=/; domain=.weibo.cn; httponly'
    'cookie':'	_T_WM=016bf14c6abc3ab59c540bcee02288ab; SUHB=0U1ZhxcAMM8pTS; PHPSESSID=02caa6775348f69a5bddee8038fdccec; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFSuQjjmcB3VQ0hDd014dYk5JpX5K-t; M_WEIBOCN_PARAMS=luicode%3D20000174; H5_INDEX=0_all; H5_INDEX_TITLE=hhhjjjqqqyyyccc; SUB=_2A254zMkIDeTxGeNI7FAY8yrFzD-IHXVYTtdArDV6PUJbvNANLWSikW1VQS1xSzeKOQbSoaDOtrPesbmJMQ..; SSOLoginState=1439218008'
    }

    return Header

def sleep(): #程序休眠,避免一次爬太多
    time.sleep(random.randint(1,5))

def getUser(citystart,cityend,pagestart,pageend):
    print 'getting users...'
    headers=header()
    user_list=[]
    the_same_city_file_text = "/home/yc/PycharmProjects/dbtest2/sina/results/user_id.txt"     #存储同城的微博用户Id及name
    city_file=open(the_same_city_file_text,"w+")
    for c in range(citystart,cityend):
        print '正在输出编号为',c,'的城市'
        for p in range(pagestart,pageend):
            print '正在输出第',p,'页的同城用户'
            url ="http://weibo.cn/find/city?province=44&city="+str(c)+"&vt=4&page="+str(p)      # 同城微博用户url
            req = urllib2.Request(url=url,headers=headers)
            text = urllib2.urlopen(req).read()
            user_id = re.compile('</td><td.*?top"><a href.*?vt=4">(.*?)<.*?粉丝(.*?)人&.*?uid=(.*?)&')          # 匹配同城微博用户的id及name
            l = user_id.findall(text)
            sleep()
            if (len(l)==0):
                print "no user id"
                return
            else:
                for item in l :
                    if int(item[1])>20:
                        # print item[1]
                        city_file.write(item[2]+"\t"+item[0]+"\n")
                        time.sleep(random.randint(1,5))
                        # print item[0]
                        # print item[2]
                        user_list.append(item[2])
                        try:
                            SinaUser.objects.get(user_id=item[2])
                        except ObjectDoesNotExist:
                            SinaUser.objects.create(user_id=item[2],user_name=item[0])
            try:
                ip_changing()
            except:
                pass
    city_file.close()
    print 'finish getting users'
    return user_list                         # 返回同城用户Id

