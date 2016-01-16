#coding=utf-8

'''
Author = Eric_Chan
Create_Time = 2015/11/7
'''

'''
社区检测
用户的详细字典构造完毕后,计算用户的情绪矩阵,计算用户的关注矩阵后加权求和后,使用BGLL算法进行社区检测
'''
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE","dbtest2.settings")
django.setup()

from AnalyzeUserMood import *
from MoodMatrix import *
from FollowMatrix import *
from Bgll import *
from LoadSQL import loadSQL
import time
from CommunityIdentification import CommunityIdentification

t1 = time.time()
loadSQL()
t2 = time.time()
print "所有数据读取完成,共花费时间为:%is"%(t2-t1)
print '-------------------------------------------------'

AnalyzeUserMood()#分析用户当日情绪
mood_matrix = GetMooodMatrix().start()
follow_matrix = GetFollowMatrix().start()
weight = mood_matrix + follow_matrix
division_result,modu = Bgll(weight).start() #获得社区检测的结果和模块度
CommunityIdentification(division_result)

# f = open("result/divisionResult.txt",'w')
# for i in division_result:
#     f.write(str(i)[1:-1]+'\n')
# f.close()
#
# f = open("result/usersMood.txt",'w')
# for ID in User.IDs:
#     f.write(str(User.Dict[ID].getMood())+',')
# f.close()

