# coding=utf-8
__author__ = 'gu'

import django, os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dbtest2.settings")
django.setup()

import time, random, urllib2, re, multiprocessing as mul, MySQLdb, cookielib, urllib, sys,chardet
from dua.models import *
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from _mysql_exceptions import ProgrammingError

from class_all_id import *

class Page(Uid):
    def __init__(self):
        Uid.__init__(self)
        self.weibo_list=[]
        self.time_list=[]
        self.weibo=[]
        self.writing_time=[]
        self.active_id=[]

    # def getId(self,text):
    #     dict_text=eval(text)
    #     self.user_list=dict_text["user_id"]
    #     return self.user_list
    #
    # def download(self):
    #     # PostData = {'number':num}
    #     request=urllib2.Request(url='http://192.168.1.41:8000/get_id',headers=self.header)
    #     response=urllib2.urlopen(request)
    #     text=response.read()
    #     dict_text = eval(text) # json转化为字典
    #     # print dict_text
    #     # print type(dict_text)
    #     self.user_list =dict_text["user_id"]
    #     # print type(user_lists)
    #     self.getPage(self.user_list,1,2)
    #     return self.user_list

    def count(self,uid,i):
        number=uid.index(i)+1
        print "第",number,"个人"


    #输入想要的用户博文页数,获取用户博文和时间并存入数据库
    def getPage(self,one_user, p1, p2):
        # try:
            print '正在储存博文和时间,开始时间:', time.time()
              # i=一个人的id
            print "id:", one_user
            one =self.one_id_text(one_user, p1, p2)  # 调用子函数,one_text本身是列表,形式([time],[weibo])

            for j in xrange(len(one[0]) - 1):
                # print 'a' , self.active_id[j]
                one_time = one[0][j + 1]  # 单条时间,博文
                one_text = one[1][j + 1]
                self.weibo_list.append(one_text) #以下三句用于写txt文件
                self.time_list.append(one_time)

            #     try:
            #         WeiboText.objects.get(user_id=self.active_id[j], time=one_time, weibo=one_text)
            #     except ObjectDoesNotExist:
            #         try:
            #             WeiboText.objects.create(user_id=i, time=one_time, weibo=one_text)
            #         except ProgrammingError:
            #             print '博文无法存入数据库'
            #             continue
            # self.write_txt(self.active_id,self.time_list,self.weibo_list)
            print '储存',one_user,'博文和时间完成'
            return True
        # except :
        #     pass
            # return time_list,weibo_list #所有人博文和时间的列表,每个人为一项,每项里有小列表


    def one_id_text(self,i, a, b):  # 传入第i个用户的id,ab为开始和结束的页数,返回这个用户的博文
        writing_time = []
        weibo = []
        dict = {}
        # reload(sys)
        # sys.getdefaultencoding('utf8')
        self.sleep()
        host_url="http://weibo.cn/u/" + str(i)
        url_request=urllib2.Request(host_url,headers=self.header)
        response=urllib2.urlopen(url_request)
        text=response.read()
        page_num = re.compile('跳页" />.*?/(.*?)页')  # 匹配微博页数
        num = page_num.findall(text)
        for nm in num:
            pm = int(nm)
            if b > pm:
                b = pm
            else:
                pass
        for k in xrange(a, b):
            if k%5==4:
                time.sleep(random.randint(0,5))
            elif k%7==6:
                self.sleep()
            else:
                pass
            print "第", k, "页"
            zyurl = "http://weibo.cn/u/" + str(i) + "?page=" + str(k)
            req = urllib2.Request(url=zyurl, headers=self.header)
            # self.sleep()
            zytext = urllib2.urlopen(req).read()
            zytext = str(zytext).decode('utf-8')
            # print zytext
            psg = re.compile('"ctt">(.*?)</span>.*?<span class="ct">(.*?)&nbsp', re.M)  # 匹配时间和正文
            passage = psg.findall(zytext)  # 一个用户所有的博文
            if (len(passage) == 0):
                print '该账号无法使用'
                self.sleep()
                k -= 1
            else:
                print "输出正常"

                for tu in passage:
                    if (re.match(U'今天', tu[1])):  # tu[1]里找到标志为今天的时间
                        if len(tu[1]) > 0:
                            # print "这是今天的博文"
                            dict.setdefault(tu[0],tu[1])

                        else:
                            pass

                    elif (re.search(U'\d分钟前', tu[1])):  # tu[1]里找到标志为几分钟前的时间
                        if len(tu[1]) > 0:
                            # print "这是今天的博文"

                            dict.setdefault(tu[0],tu[1])  # 键为tu[0],即是博文,值为tu[1],即是时间
                        else:
                            pass
                    else:
                        print "这不是今天的博文"
                        pass

                for item0,item1 in dict.items():  # item0为tu[0],博文.  item1为tu[1],时间
                    # print item0,item1

                    # t=tu[1].encode('gbk')
                    # print t,'time________________________'
                    extra1 = re.compile('</span>.*$')  # 匹配输入字符串的结束位置
                    # extra2=re.compile('</span>.*?</a>')
                    today = re.compile(u'今天')
                    ago = re.compile(u'\d分钟前')
                    wbtime = re.sub(extra1, ' ', item1) # 在tu[1]中把extra1都用空格替换掉
                    # print wbtime

                    t = time.strftime('%m' + '月' + '%d' + '日', time.localtime())
                    t = t.decode('utf-8')

                    wbtime = re.sub(today, t, wbtime)
                    wbtime = re.sub(ago,t,wbtime)

                    # wbtime,gb2312,type str
                    writing_time.append(wbtime)

                    # print "第",passage.index(tu)+1,"篇博文,发表时间",time
                    # content=tu[0].encode('gbk','ignore') #gbk就是字符串
                    sub_title = re.compile(u'<img.*?注')
                    tag = re.compile('</a>')  # 去除标签
                    link = re.compile('<a href=.*?>|http.*?</a>')  # 去除链接
                    content = re.sub(link, " ", item0)
                    content = re.sub(tag, '', content)
                    content = re.sub(sub_title, '', content)
                    content = content.encode('utf-8', 'ignore')
                    weibo.append(content)
                    if len(weibo)>0:
                        self.active_id.append(i)

                    print i,wbtime, "发表动态"  # 输出当天的博文和时间
        return writing_time, weibo # 一个人的博文,列表形式,每一条博文为一项,活跃的用户列表


                # for tu in passage:
                #     # t=tu[1].encode('gbk')
                #     # print t,'time________________________'
                #     extra1 = re.compile('</span>.*$')
                #     # extra2=re.compile('</span>.*?</a>')
                #     today = re.compile(u'今天')
                #     ago=re.compile(u'\d分钟前')
                #     wbtime = re.sub(extra1, ' ', tu[1])
                #     t = time.strftime('%m' + '月' + '%d' + '日', time.localtime())
                #     t = t.decode('utf-8')
                #     wbtime = re.sub(today, t, wbtime)
                #     wbtime=re.sub(ago,t,wbtime)
                #     # time=re.sub(extra2,' ',time)
                #     # wbtime,gb2312,type str
                #     writing_time.append(wbtime)
                #     # print "第",passage.index(tu)+1,"篇博文,发表时间",time
                #     # content=tu[0].encode('gbk','ignore') #gbk就是字符串
                #     sub_title = re.compile(u'<img.*?注')
                #     tag = re.compile('</a>')  # 去除标签
                #     link = re.compile('<a href=.*?>|http.*?</a>')  # 去除链接
                #     content = re.sub(link, " ", tu[0])
                #     content = re.sub(tag, '', content)
                #     content = re.sub(sub_title, '', content)
                #     content = content.encode('utf-8', 'ignore')
                #     weibo.append(content)



    #与getPage联合发动,写入txt,可禁用或开启
    def write_txt(self,uid,time_list,weibo_list): #一个人的id和他的时间,微博列表
        zipper=zip(time_list,weibo_list)
        print uid,' 正在写入博文'
        if uid is not None:
            not_number=re.compile('\D')
            uid=re.sub(not_number,'', str(uid))
            file=open(self.text_dir+'uid='+str(uid)+'.txt','w+')
        else:
            file=open(self.text_dir+self.default_title +'.txt','w+')

        for i in zipper:
            time=i[0]
            weibo=i[1]
            time=time.encode('utf-8','ignore')
            file.write(uid+','+time+','+weibo+'\n')
        file.close()
        print uid,' 完成输入博文'
