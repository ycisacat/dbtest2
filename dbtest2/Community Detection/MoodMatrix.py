#coding=utf-8

'''
Author = Eric_Chan
Create_Time = 2015/11/7
'''

'''
根据用户的情绪,分析获得用户-用户的情绪矩阵,(若用户1与用户2情绪相同弄个,则 matrix(1,2)=matrix(2,1)=1
输入:用户字典
输出:用户SY-用户SY-权值  userNum*3的矩阵
'''
from WeiboUser import *
import numpy as np
import time
class GetMooodMatrix:
    def __init__(self):
        self.team = {0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[]} #若用户情绪相同则分为同一个组
        #0:'厌恶',1:'同情',2:'喜欢',3:'怨恨',4:'悲伤',5:'愉快',6:'愤怒',7:'焦虑',8:'其他'
        self.mood_matrix = []

    def __devideTeam(self): #根据用户的情绪划分小组
        for i in range(User.Num):
            try:
                self.team[User.Dict[User.IDs[i]].getMood()].append(i)
            except:
                pass


    def __createMoodMatrix(self):
        for t in range(8):#除'其他'情绪以外,当用户1与用户2的情绪相同时,mood_matrix[?]=[1,2,1]
            for i in self.team[t]:
                for j in self.team[t]:
                    if(i!=j):
                        line = [i,j,1]
                        self.mood_matrix.append(line)

    def start(self):
        start = time.time()
        self.__devideTeam()
        self.__createMoodMatrix()
        end = time.time()
        print "用户-用户情绪矩阵构造完毕,花费时间为:" ,end-start,'s'
        return self.mood_matrix

