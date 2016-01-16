#coding=utf-8

'''
Author = Eric_Chan
Create_Time = 2015/11/8
'''

import MySQLdb
from WeiboUser import *
import sys

def loadSQL():

    print "开始连接数据库...",
    sys.stdout.write('\r')
    # 打开数据库连接
    db= MySQLdb.connect(

        # host='192.168.1.41',
        # port = 3306,
        # user='yc',
        # passwd='uliuli520',
        # db ='sina',
        # charset='utf8',

        host='192.168.235.36',
        port = 3306,
        user='fig',
        passwd='fig',
        db ='fig',
        charset='utf8',)

    cursor = db.cursor()
    print "数据库连接成功"

    #获取Id-用户名 构建用户字典
    print "构造用户名单...",
    sys.stdout.write('\r')
    cursor.execute("SELECT * from sinauser")
    data = cursor.fetchall()
    for row in data:
        id = row[1]
        name = row[2]
        id = int(id)
        User(id=id,name=name)
        if User.Num>=1000:
            break
    print "用户名单构造完毕,共有%i名用户"%User.Num

    #获取每个用户的关注用户,若不在用户名单 则忽略,接着下一个数据的读取
    print "读取用户的关注名单...",
    sys.stdout.write('\r')
    cursor.execute("SELECT * from gdfollow")
    data = cursor.fetchall()
    for row in data:
        user_id = int(row[1])   #用户的ID
        follow_id = int(row[2]) #该用户关注的用户的ID
        try:
            User.Dict[user_id].addFollows(follow_id)
        except:
            print "      id:",user_id," 的用户不在用户名单中,关注名单写入失败"
    print "所有用户的关注写入完成"

    #获取每个用户的关注用户,若不在用户名单 则忽略,接着下一个数据的读取
    print "读取用户的粉丝名单...",
    sys.stdout.write('\r')
    cursor.execute("SELECT * from gdfan")
    data = cursor.fetchall()
    for row in data:
        user_id = int(row[1])   #用户的ID
        fan_id = int(row[2]) #该用户的粉丝的ID
        try:
            User.Dict[user_id].addFans(fan_id)
        except:
            print "      id:",user_id," 的用户不在用户名单中,粉丝名单写入失败"
    print "所有用户的粉丝写入完成"

    # 获取每个用户的博文,每篇博文由博文内容和博文发布的时间构成
    print "读取用户的所有博文...",
    sys.stdout.write('\r')
    cursor.execute("SELECT * from weibotext")
    data = cursor.fetchall()
    for row in data:
        user_id = int(row[1]) #发博文的用户ID
        text = row[2]    #单条博文
        time = row[3]    #该博文发布的时间
        unit_blog = Blog(text=text,time=time)
        try:
            User.Dict[user_id].addBlog(unit_blog=unit_blog)
        except:
            print "      id:",user_id," 的用户不在用户名单中,博文写入失败"
    print "所有用户的博文写入完成"

    db.close() # 关闭数据库连接
