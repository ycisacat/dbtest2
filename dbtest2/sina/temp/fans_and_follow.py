# coding:utf-8      #是用来指定文件编码为utf-8的
from sina.temp import universal as uni

__author__ = 'gu'
import re
import urllib2
import time
import random
from dua.models import *
from django.core.exceptions import ObjectDoesNotExist




def getFans(Userid,fanspagestart,fanspageend):                                    #爬粉丝的id及name,
    print "getting fans"
    headers=uni.header()
    fans_list=[]
    gd_fans = []
    for i in Userid:
        for j in range(fanspagestart,fanspageend):
            crawler_fans_url = "http://weibo.cn/"+i+"/fans?page="+str(j)           #第ele个人的第j页粉丝链接
            # print crawler_fans_url
            req_fans= urllib2.Request(url=crawler_fans_url,headers=headers)
            fans_text = urllib2.urlopen(req_fans).read()
            fans_id = re.compile('<img.*?<a href=.*?u.([1-9][0-9]{9})">(.*?)<')     #匹配粉丝的id和name
            fans = fans_id.findall(fans_text)
            if (len(fans)==0):
                print "全部粉丝列表为空"
                return gd_fans
            else:
                for item in fans:
                    fans_list.append(item[0])

                    fans_home_page_url = "http://weibo.cn/"+item[0]                        #即将进行判断是否广东的粉丝的链接
                    req_fans_home_page = urllib2.Request(url=fans_home_page_url,headers=headers)
                    fans_homepage_text = urllib2.urlopen(req_fans_home_page).read()

                    judge_fans_add = re.compile('/广东.*?uid=(.*?)&')#判断是不是广东,匹配广东匹配成功，返回粉丝id，不成功，则不返回
                    fans_add = judge_fans_add.findall(fans_homepage_text)
                    for k in fans_add:
                        while fans_add.count(k)>1:
                            del fans_add[fans_add.index(k)]
                        print k+"粉丝"
                        try:
                            GDFan.objects.get(user_id=i)
                        except ObjectDoesNotExist:
                            GDFan.objects.create(user_id=i,gdfans_id=k)
                        gd_fans.append(i[1])
                        gd_fans.append(k)
                        uni.sleep()
            uni.sleep()
    return gd_fans                                            #返回过滤后只剩广东的粉丝ID


def getFollow(Userid,followpagestart,followpageend):
    print 'getting follow'
    headers=uni.header()
    follow_list = []
    gd_follow = []
    for i in Userid:
        for j in range(followpagestart,followpageend):
            crawler_follow_url = "http://weibo.cn/"+i+"/follow?page="+str(j)          #第ele个人的第j页关注链接
            reqfollow= urllib2.Request(url=crawler_follow_url,headers=headers)
            follows_text = urllib2.urlopen(reqfollow).read()

            follows_id = re.compile('top"><a href=.*?>(.*?)<.*?uid=(\d\d+)&')          #匹配没过滤的关注的人的id和name
            follows = follows_id.findall(follows_text)
            if (len(follows)==0):
                print '全部关注列表为空'
                return gd_follow
            else:
                for item in follows:
                    time.sleep(random.randint(1,5))
                    follow_list.append(item[1])
                    follows_homepage_url = "http://weibo.cn/"+item[1]                       #即将进行判断是否广东的关注链接
                    req_follows_homepage = urllib2.Request(url=follows_homepage_url,headers=headers)
                    fans_homepage_text = urllib2.urlopen(req_follows_homepage).read()

                    judge_follows_add = re.compile('/广东.*?uid=(.*?)&')#判断是不是广东,匹配广东匹配成功，返回粉丝id，不成功，则不返回
                    fans_add = judge_follows_add.findall(fans_homepage_text)
                    for k in fans_add:
                        while fans_add.count(k)>1:
                                del fans_add[fans_add.index(k)]
                        print k+"关注"
                        uni.sleep()
                        gd_follow.append(k)
                        try:
                            GDFollow.objects.get(user_id=i)
                        except ObjectDoesNotExist:
                            GDFollow.objects.create(user_id=i,gdfans_id=k)

        uni.sleep()
    return gd_follow                                            #返回过滤后的关注id


