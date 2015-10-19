# coding:utf-8      #是用来指定文件编码为utf-8的
from sina.temp import universal as uni

__author__ = 'gu'
import re
import urllib2
from dua.models import *
from django.core.exceptions import ObjectDoesNotExist


def getFans(Userid,fanspagestart,fanspageend):                                       # 爬粉丝的id及name,
    print 'getting fans...'
    headers=uni.header()
    the_fans_text = "/home/yc/PycharmProjects/dbtest2/sina/results/fans_id.txt"   #存储全部粉丝的Id及name
    fans_file = open(the_fans_text,"w+")
    gd_fans_txt = "/home/yc/PycharmProjects/dbtest2/sina/results/gd_fans.txt"     #存储过滤后广东粉丝的Id及name
    gd_fans_file = open(gd_fans_txt,"w+")
    fans_list=[]
    gd_fans = []
    for i in Userid:
        print '用户： ',i
        for j in range(fanspagestart,fanspageend):
            crawler_fans_url = "http://weibo.cn/"+i+"/fans?page="+str(j)           # 第ele个人的第j页粉丝链接
            # print crawler_fans_url
            req_fans= urllib2.Request(url=crawler_fans_url,headers=headers)
            fans_text = urllib2.urlopen(req_fans).read()
            uni.sleep()
            fans_id = re.compile('<br/>粉丝(.*?)人.*?uid=(.*?)&')     # 匹配粉丝数大于20人的粉丝的id
            fans = fans_id.findall(fans_text)
            if (len(fans)==0):
                print "全部粉丝列表为空"
                return gd_fans
            else:
                for item in fans:
                    if int(item[0])>20:
                        # print type(item[0])
                        # print item[0] +'粉丝数'
                        # print item[1]
                        fans_file.write(i+"\t"+item[1]+"\n")                              #没过滤掉的粉丝写入FansFile
                        fans_list.append(item[1])

                        fans_home_page_url = "http://weibo.cn/"+item[1]                        # 即将进行判断是否广东的粉丝的链接
                        req_fans_home_page = urllib2.Request(url=fans_home_page_url,headers=headers)
                        fans_homepage_text = urllib2.urlopen(req_fans_home_page).read()
                        uni.sleep()
                        judge_fans_add = re.compile('/广东.*?uid=(.*?)&') # 判断是不是广东,匹配广东匹配成功，返回粉丝id，不成功，则不返回
                        fans_add = judge_fans_add.findall(fans_homepage_text)
                        for k in fans_add:
                            while fans_add.count(k)>1:
                                del fans_add[fans_add.index(k)]
                            print k+"粉丝"
                            gd_fans_file.write(i+"\t"+k+"\n")        #过滤后的粉丝写入GDFansFile

                            try:
                                GDFan.objects.get(gdfans_id=k)
                            except ObjectDoesNotExist:
                                GDFan.objects.create(user_id=i,gdfans_id=k)
                            gd_fans.append(k)
            try:
                uni.ip_changing()
            except:
                pass
    fans_file.close()                                         #没有过滤的粉丝文件关闭
    gd_fans_file.close()                                       #过滤后的粉丝文件关闭
    print 'finish getting fans'
    return gd_fans      # 返回过滤后只剩广东的粉丝ID


def getFollow(Userid,followpagestart,followpageend):
    print 'getting follow...'
    headers=uni.header()
    the_follow_text = "/home/yc/PycharmProjects/dbtest2/sina/results/follow_id.txt"     #存储全部关注的Id及name
    follow_file = open(the_follow_text,"w")
    only_gd_follow = "/home/yc/PycharmProjects/dbtest2/sina/results/gd_follow.txt"     #存储过滤后广东关注的Id及name
    gd_follow_file = open(only_gd_follow,"w")
    follow_list = []
    gd_follow = []
    for i in Userid:
        print '用户： ',i
        for j in range(followpagestart,followpageend):
            crawler_follow_url = "http://weibo.cn/"+i+"/follow?page="+str(j)          # 第ele个人的第j页关注链接
            reqfollow= urllib2.Request(url=crawler_follow_url,headers=headers)
            follows_text = urllib2.urlopen(reqfollow).read()
            follows_id = re.compile('<br/>粉丝(.*?)人.*?uid=(\d\d+)&')          # 匹配没过滤粉丝数大于20的关注的人的id
            follows = follows_id.findall(follows_text)
            if len(follows)==0:
                print '全部关注列表为空'
                return gd_follow
            else:
                uni.sleep()
                for item in follows:
                    if int(item[0])>20:
                        # print item[0]+'粉丝数'
                        # print item[1]
                        follow_file.write(i+"\t"+item[1]+"\n")                               #没过滤的关注写入FollowFile

                        follow_list.append(item[1])
                        follows_homepage_url = "http://weibo.cn/"+item[1]                       # 即将进行判断是否广东的关注链接
                        req_follows_homepage = urllib2.Request(url=follows_homepage_url,headers=headers)
                        fans_homepage_text = urllib2.urlopen(req_follows_homepage).read()

                        uni.sleep()
                        judge_follows_add = re.compile('/广东.*?uid=(.*?)&') # 判断是不是广东,匹配广东匹配成功，返回粉丝id,不成功,则不返回
                        fans_add = judge_follows_add.findall(fans_homepage_text)
                        for k in fans_add:
                            while fans_add.count(k)>1:
                                    del fans_add[fans_add.index(k)]
                            print k+"关注"
                            gd_follow_file.write(i+"\t"+k+"\n")          #过滤后的关注写入GDFollowFile

                            gd_follow.append(k)
                            try:
                                GDFollow.objects.get(gdfollows_id=k)
                            except ObjectDoesNotExist:
                                GDFollow.objects.create(user_id=i,gdfollows_id=k)
    follow_file.close()                                          #没有过滤的关注文件关闭
    gd_follow_file.close()                                        #过滤后的关注文件关闭
    print 'finish getting follows'
    return gd_follow                                            # 返回过滤后的关注id


