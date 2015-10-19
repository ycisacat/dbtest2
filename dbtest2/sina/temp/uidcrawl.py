#coding=utf-8
__author__ = 'yc'
import re
import urllib2

from django.core.exceptions import ObjectDoesNotExist

import universal as uni
from dua.models import *
import sina.temp.writingtxt as wr

# def getUrl(a,b,c,d): #获取粉丝页中用户主页的链接
#         print "getting url"
#         s=[]
#         for k in range(a,b):
#             print "正在输出编号为",k,"的城市的粉丝"
#             for i in range(c,d):
#                 print "正在输出第",i,"页的粉丝链接"
#                 # cookieJar=cookielib.MozillaCookieJar(os.path.join('crawltest1.py'))
#                 url="http://weibo.cn/find/city?province=44&city="+str(k)+"&page="+str(i)+"&vt=4" #同城用户页
#                 headers=uni.header()
#                 req= urllib2.Request(url=url,headers=headers)
#                 text=urllib2.urlopen(req).read()                #从headers开始为伪装成浏览器进行访问
#                 text=str(text).decode('utf-8')
#                 # print "text",text
#                 link_pat=re.compile(u"<br/>粉丝(.*?)人.*?uid=(.*?)&amp;")  #匹配粉丝数和uid
#                     # ("/attention/add\?uid=(.*?)&amp")  #匹配uid
#                  #(/(?!http|find|attention).*?[^(amp;)]vt=4)"')
#                 l=link_pat.findall(text)
#                 # print "l",l
#                 for i in l:
#                     if i[0]>20:         #去除僵尸粉
#                         # print i[1]
#                         s.append(i[1])  #s为真实粉的id表
#                 if (d-c>7):
#                     sleep()
#         if (len(s)==0):
#             print "没有获取到链接"
#         return s  #用户id列表

def getPage(u,p1,p2):  # 传入主页链接,开始页数和结束页数
    print 'getting page...'
    print "总共有",len(u),"人"
    weibo_list=[]
    time_list=[]
    for i in u: #i=一个人的id
        print "第",u.index(i)+1,"个人,id:",i
        one=one_id_text(i,p1,p2) #调用子函数,one_text本身是列表,形式([time],[weibo])
        print 'aaa',len(one[0]),len(one[1]) #11,11
        for j in range(len(one[0])-1): #j取0-19
            one_time=one[0][j+1] #单条时间,博文
            one_text=one[1][j+1]
            print 'ttt',one_time
            print 'www',one_text
            try:
                WeiboText.objects.get(user_id=i,time=one_time,weibo=one_text)
            except ObjectDoesNotExist:
                try:
                    WeiboText.objects.create(user_id=i,time=one_time,weibo=one_text)
                except:
                    print '无法存入数据库'
                pass
            weibo_list.append(one_text)
            time_list.append(one_time)
            wr.write_txt(i,time_list,weibo_list)
    print 'finish getting page'
    return time_list,weibo_list #所有人博文和时间的列表,每个人为一项,每项里有小列表

def one_id_text(i,a,b):   #传入第i个用户的id,ab为开始和结束的页数,返回这个用户的博文
        weibo=[]
        writing_time=[]
        for k in range(a,b):
            print "第",k,"页"
            zyurl="http://weibo.cn/u/"+str(i)+"?page="+str(k)
            headers=uni.header()
            req=urllib2.Request(url=zyurl,headers=headers)
            uni.sleep()
            zytext=urllib2.urlopen(req).read()
            zytext=str(zytext).decode('utf-8')
            psg=re.compile('"ctt">(.*?)</span>.*?<span class="ct">(.*?)&nbsp',re.M)  # 匹配时间和正文
            passage=psg.findall(zytext)  #一个用户所有的博文
            if (len(passage)==0):
                print "没有get到内容,可能cookie出错"
                return writing_time,weibo
            else:
                print "输出正常"
                for tu in passage:
                    # t=tu[1].encode('gbk')
                    extra1=re.compile('</span>.*$')
                    # extra2=re.compile('</span>.*?</a>')
                    time=re.sub(extra1,' ',tu[1])
                    # time=re.sub(extra2,' ',time)
                    time=time.encode('utf-8')
                    writing_time.append(time)
                    # print "第",passage.index(tu)+1,"篇博文,发表时间",time
                    # content=tu[0].encode('gbk','ignore') #gbk就是字符串
                    sub_title=re.compile(u'<img.*?注')
                    tag=re.compile('</a>') #去除标签
                    link=re.compile('<a href=.*?>|http.*?</a>') #去除链接
                    content=re.sub(link," ",tu[0])
                    content=re.sub(tag,'',content)
                    content=re.sub(sub_title,'',content)
                    content=content.encode('utf-8','ignore')
                    weibo.append(content)
            if (b-a>3):
                uni.sleep()
            try:
                uni.ip_changing()
            except:
                pass
        print 'time',len(writing_time)
        print 'weibo',len(weibo)
        return writing_time,weibo #一个人的博文,列表形式,每一条博文为一项

# def offer(uid,bp,ep):
#     q=mul.Queue(3)   # 表示队列中可以存放对象的最大数量为3
#     q.put(getPage(uid,bp,ep))
#     qq=q.get()  #这两句用于写txt文件
#     print 'qq',qq
#     w=wr.tupling(uid,qq[0],qq[1])  #如果要写入文件,这两句#号要取消
#     return True



