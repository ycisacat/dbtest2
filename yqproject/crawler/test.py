# coding=utf-8
import re

__author__ = 'yc'
# class A():
#     def __init__(self):
#         self.a = []
#
#     def test(self):
#         b = [1,2,3,4,5]
#         c = [5,6,7,8,9]
#
#         e = []
#
#         for i in range(3):
#             print self.a
#
#             for j in c:
#                 if j not in self.a:
#                     print '不在'
#                     e.append(j)
#                 else:
#                     print "zai"
#             self.a += e
#         print self.a
#
# A().test()
# print len(c)
# for i in range(0,len(c)):
#     print c[i][0]
# result_num = [1]
# if result_num:
#     result_num.append(1)
# else:
#     result_num.append(2)
#
# print result_num


# blogstr ='【年轻人广场玩“彩虹跑” 满地粉末愁坏清洁工】近日，一群青年在成都萃锦西路的公共广场开展“彩虹跑”活动，留下一片狼藉，地面遍布彩色粉末，风一吹便扬起粉尘。如何清理难坏清洁工。主办方称粉末是染色玉米粉，有人清理，但直到清洁工清理完毕，也未见商家工作人员来清扫。年轻人广场上玩“彩虹跑” 满地粉末愁怀清洁工 [组图共2张]'
# topic_patternts = re.compile('#(.*?)# |【(.*?)】')
# topic = topic_patternts.findall(blogstr)
# print len(topic)
# if len(topic):
#
#     topic = [topic[0][0]+topic[0][1]]
#
#     print 'ss',topic[0]


def tt():
    t1 = [1,2,3,4,5]
    t2 = [2,3,4,5,5]
    t3 = [4,5,6,7,5]

    return t1,t2,t3

t = tt()
print t
print '博文',t[2]
z = zip(t[0],t[1],t[2])
print len(z)
for i in range(len(z)):
    print z[i]

