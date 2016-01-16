#coding=utf-8

'''
Author = Eric_Chan
Create_Time = 2015/11/5
'''

'''
该类用来记录微博用户的ID,博文,关注用户的ID,粉丝用户的ID
'''

class User:

    Dict = {} #用来记录所有用户的字典,用户的ID作为字典的keys
    IDs = []  #记录所有用户的ID
    Num = 0  #用户数

    def __init__(self,id,name): #用户的ID和用户名在实例化后便固定不能修改
        self.id = id
        self.name = name
        self.blog = [] #用户发的博文
        self.fans = [] #用户的粉丝
        self.follows = [] #用户的关注
        self.mood = -1 #记录用户当日的情绪 0:'厌恶',1:'同情',2:'喜欢',3:'怨恨',4:'悲伤',5:'愉快',6:'愤怒',7:'焦虑',8:'其他'
        User.Dict[id] = self
        User.Num += 1
        # for i in range(User.Num):
        #     try:
        #         if User.IDs[i] > id:
        #             User.IDs.insert(i,id)
        #             break
        #     except:
        #         if (i==User.Num-1):
        #             User.IDs.append(id)
        #             break
        User.IDs.append(id)

    def getName(self):
        return self.name

    def setBlog(self,blog):
        self.blog = blog

    def getBlog(self):
        return self.blog

    def addBlog(self,unit_blog):
        self.blog.append(unit_blog)

    def setFans(self,fans):
        self.fans = fans

    def getFans(self):
        return self.fans

    def addFans(self,unit_fan):
        self.fans.append(unit_fan)

    def setFollows(self,follows):
        self.follows = follows

    def getFollows(self):
        return self.follows

    def addFollows(self,unit_follow):
        self.follows.append(unit_follow)

    def setMood(self,mood):
        self.mood = mood

    def getMood(self):
        return self.mood

class Blog:
    def __init__(self,text,time):
        self.time = time     #博文发布的时间
        self.text = text     #博文的内容

    def getTime(self):
        return self.time

    def getText(self):
        return self.text



