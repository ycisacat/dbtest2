#coding=utf-8
__author__ = 'yc'
import re
import chardet
import multiprocessing as mul

# def tupling(u,t,p): #u为用户id,t为时间,p为博文
#     print 'tupling'
#     print 'aaa',len(t),len(p)
#     mix=[]
#     for i in range(len(u)):  #i=人数
#         print '第',i+1,'人'
#         temp_mix=[]
#         for j in range(len(p[i])-1): #j=博文数
#             print 'bbb',len(t[i]),len(p[i])
#             # print 't[i][j]',t[i][j]
#             x=(u[i],t[i][j+1],p[i][j+1]) #encoding=utf-8,type'str'
#             # x[1].decode('gbk','ignore').encode('utf-8','ignore')
#             # x[2].decode('gbk','ignore').encode('utf-8','ignore')
#             temp_mix.append(x)  #一个人的全部带时间博文列表,每一项为同一个人的不同条目
#         mix.append(temp_mix)#全部人的列表,每一项为一个人的全部时间,博文
#     write_txt(mix)
#     return mix   #返回所有人的博文和时间,每人为一项,[[(' ',' ',' ')]]

def write_txt(uid,t,p): #一个人的id和他的时间,微博列表
    print '正在写入博文'
    print 'txt',len(t),len(p)
    default_title ="anonymous"
    # for k in mix: #每一个人的(全部)
    #     # for kk in k:  #的每一条带时间的博文和id
    #     #      if kk is not None:  #kk是元组
    #              uid=str(k[0][0])
    if uid is not None:
        not_number=re.compile('\D')
        uid=re.sub(not_number,'', uid)
        file=open('/home/yc/PycharmProjects/dbtest2/sina/blogtext/'+'uid='+uid+'.txt','w+')
    else:
        file=open('/home/yc/PycharmProjects/dbtest2/sina/blogtext/'+default_title +'.txt','w+')
    for i in range(len(t)):
        time=str(t[i])
        weibo=str(p[i])
        file.write(uid+'\t'+time+'\t'+weibo+'\n')
    file.close()
    print '完成输入博文'

# def wb_db(mix):  #正式代码,把打包好的uid,时间,博文导入数据库
#     from dua.models import WeiboText
#     print mix
#     for i in mix:
#         for ii in i:
#             uid=ii[0]
#             time=ii[1]
#             weibo=ii[2]
#             WeiboText.objects.create(uid=uid,writing_time=time,weibo=weibo)
#     print 'success'
#
# def fans_db(): #文件导入式
#     from dua.models import GDFans
#     f=open('/home/yc/PycharmProjects/dbtest2/sina/results/gd_fans.txt')
#     for line in f:
#         uid,fans=line.strip().split('\t')
#         GDFans.objects.create(uid=uid,gdfans=fans)
#     f.close()
#
# def follows_db():
#     from dua.models import GDFollows
#     f=open('/home/yc/PycharmProjects/dbtest2/sina/results/gd_follow.txt')
#     for line in f:
#         uid,follow=line.strip().split('\t')
#         GDFollows.objects.create(uid=uid,gdfollows=follow)
#     f.close()
