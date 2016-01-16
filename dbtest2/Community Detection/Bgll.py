#coding=utf-8

'''
Author = Eric_Chan
Create_Time = 2015/11/7
'''

'''
使用igraph中的BGLL算法对社区进行社区检测
输入用户-用户权值矩阵
输出社区检测结果和社区模块度
'''
import igraph
from WeiboUser import *
import time
import sys

class Bgll:
    def __init__(self,usersLink):
        self.usersLink = usersLink

    def __createGraph(self):
        g = igraph.Graph(User.Num)#首先构建点的个数为用户数目的图
        weights = []
        edges = []
        for line in self.usersLink:
            edges += [(line[0],line[1])]
            weights.append(line[2])
        g.add_edges(edges)
        return g,weights

    def start(self):
        start2 = time.time()
        print "开始划分社区..."
        graph,weights = self.__createGraph()
        BGLL_result = graph.community_multilevel(weights=weights)#社区划分结果
        end2 = time.time()
        print "划分完成,花费时间为: ", end2 - start2 ,'s'

        mmm = BGLL_result.modularity#社区模块度
        # print 'louvain社区探测算法' , '\n',BGLL_result , '\n'
        # print "社区模块度:", mmm
        return BGLL_result,mmm

