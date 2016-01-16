#coding=utf-8

'''
Author = Eric_Chan
Create_Time = 2015/11/7
'''

'''
根据用户的关注,分析用户的关注矩阵,若用户1关注用户2,则matrix(1,2)=1(非对称矩阵)
输入:用户字典
输出:用户SY-用户SY-权值  UserNum*3 矩阵
'''

from WeiboUser import *
import numpy as np
import time

class GetFollowMatrix:
    def __init__(self):
        self.follow_matrix = []

    def __createFollowMatrix(self):
        for i in range(User.Num):
            follow_users = User.Dict[User.IDs[i]].getFollows() #关注的用户
            for j in follow_users:
                try:#若关注的用户在用户名单中,则为这2个用户 添加权值
                    line = [i,User.IDs.index(j),1]
                    self.follow_matrix.append(line)
                except:
                    continue

    def start(self):
        start = time.time()
        self.__createFollowMatrix()
        end = time.time()
        print "用户-用户关注矩阵构建完毕,花费时间为:" ,end - start,'s'
        return self.follow_matrix
