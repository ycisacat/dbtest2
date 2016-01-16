#coding=utf-8

'''
Author = Eric_Chan
Create_Time = 2015/11/6
'''

'''
分析用户每条博文,计算用户的情绪值,取情绪值最大的作为该用户的情绪.
面向对象
输入:用户字典
输出:每个用户的情绪
'''
from WeiboUser import *
import jieba
import time
import sys
jieba.initialize()
time.sleep(1)

class AnalyzeUserMood:
    def __init__(self):
        self.disgust_words = self.__loadData('disgust')   #情绪为厌恶的词
        self.sympathy_words = self.__loadData('sympathy') #情绪为同情的词
        self.like_words = self.__loadData('like')         #情绪为喜欢的词
        self.hate_words = self.__loadData('hate')         #情绪为怨恨的词
        self.sad_words = self.__loadData('sad')           #情绪为悲伤的词
        self.happy_words = self.__loadData('happy')       #情绪为愉快的词
        self.angry_words = self.__loadData('angry')       #情绪为愤怒的词
        self.anxiety_words = self.__loadData('anxiety')   #情绪为焦虑的词
        self.symbol_words = self.__loadData('symbol')     #标点符号
        self.privative_words = self.__loadData('privative') #否定词
        self.__start()


    def __loadData(self,fileName): #读取文字
        file1 = open('emotion_words/%s.txt'%fileName,'r')
        line = file1.readline().strip()
        words = []
        while line:
            line = line.decode('utf-8')
            words.append(line)
            line = file1.readline().strip()
        file1.close()
        return words

    def __privativeWordsAnalyze(self,sentence):#否定词分析 输入已分词的单篇博文
        words_list = {}
        l = len(sentence)
        for i in range(l):
            if sentence[i] in self.privative_words:
                words_list[i] = sentence[i]

        keys = words_list.keys()
        keys.sort()

        #否定词处理1：若否定词出现在句末，则忽略。   (例：‘我很开心，好不？’  否定词‘不’并没有改变句意)
        for j in keys:
            if (j>=l-2):
                del words_list[j]
                del keys[keys.index(j)]

        #否定词处理2：除去句末的否定词后，若仍存在多个否定词（双重否定），则作为普通句子继续匹配
        canReturn = True #是否可以返回
        if (len(words_list)>=2):
            for j in range(len(keys)-1):
                _bool = False
                temp = sentence[keys[j]:keys[j+1]]
                for i in range(len(temp)):
                    if temp[i] in self.symbol_words:#判断连续2个否定词中是否存在标点
                        _bool = True
                        canReturn = False
                        break

                if ((_bool==False)&(j==(len(keys)-2))&(canReturn==True)):#若不存在标点，且为最后一对否定词，则忽略并返回继续运行
                    return sentence
                elif (_bool==False):    #若不存在标点，但不为最后一对，则删了这对否定词，继续进行下一组的否定词的判断
                    if words_list.has_key(keys[j]):
                        del words_list[keys[j]]
                    del words_list[keys[j+1]]
                    canReturn = False   #2个否定词之间存在标点，不能返回，必须接下来处理

        #否定词处理3：否定词前后出现的情绪词，作为中性词处理
        keys = words_list.keys()#重新获得处理过后的所有否定词的索引
        for j in keys:
            if j>0:
                sentence[j-1:j+3] = [0]*4 #将否定词的前一位和后一位包括自身的所有词条都归为0（中性词）
            if j==0:
                sentence[j:j+2] = [0]*3
        return sentence

    def __userMoodAnalyze(self,originText): #输入 用户-日发博文 输出该用户该日的情绪
        l = len(originText) #用户日发博文
        user_mood = [0 for k in range(9)] #构建情绪值矩阵
        for i in range(l):#对该用户的每条博文进行分析
            privative_anlyzed = False #该博文是否进行过否定分析
            mood_matrix = [0 for k in range(8)] #建立 博文-八大情绪矩阵 顺序为 0：厌恶  1：同情  2：喜欢  3：怨恨  4：悲伤  5：愉快  6：愤怒  7：焦虑
            if originText[i].getTime().startswith("10") == False:
                continue
            text_list = list(jieba.cut(originText[i].getText(),cut_all=False))
            for j in range(len(text_list)):#对博文的每条词条进行分析，若存在在词库中，则在对应情绪值 加1
                if text_list[j] in self.symbol_words:#若该词条为标点符号则跳过情绪判断
                    continue
                if (text_list[j] in self.privative_words)&(privative_anlyzed == False):#若该词为否定词，则对该语句进行否定处理
                    text_list = self.__privativeWordsAnalyze(text_list)
                    privative_anlyzed = True
                    continue
                if text_list[j] in self.disgust_words:
                    try:                                   #若该字条非第一个字条
                        if text_list[j-1] == '[':               #且上一个字条为 '['
                            mood_matrix[0] = mood_matrix[0] + 3 #可判断为表情，情绪值另+3.
                    except:
                        pass
                    mood_matrix[0] = mood_matrix[0] + 1         #普通的情绪词则情绪值+1
                elif text_list[j] in self.sympathy_words:
                    try:
                        if text_list[j-1] == '[':
                            mood_matrix[1] = mood_matrix[1] + 3
                    except:
                        pass
                    mood_matrix[1] = mood_matrix[1] + 1
                elif text_list[j] in self.like_words:
                    try:
                        if text_list[j-1] == '[':
                            mood_matrix[2] = mood_matrix[2] + 3
                    except:
                        pass
                    mood_matrix[2] = mood_matrix[2] + 1
                elif text_list[j] in self.hate_words:
                    try:
                        if text_list[j-1] == '[':
                            mood_matrix[3] = mood_matrix[3] + 3
                    except:
                        pass
                    mood_matrix[3] = mood_matrix[3] + 1
                elif text_list[j] in self.sad_words:
                    try:
                        if text_list[j-1] == '[':
                            mood_matrix[4] = mood_matrix[4] + 3
                    except:
                        pass
                    mood_matrix[4] = mood_matrix[4] + 1
                elif text_list[j] in self.happy_words:
                    try:
                        if text_list[j-1] == '[':
                            mood_matrix[5] = mood_matrix[5] + 3
                    except:
                        pass
                    mood_matrix[5] = mood_matrix[5] + 1
                elif text_list[j] in self.angry_words:
                    try:
                        if text_list[j-1] == '[':
                            mood_matrix[6] = mood_matrix[6] + 3
                    except:
                        pass
                    mood_matrix[6] = mood_matrix[6] + 1
                elif text_list[j] in self.anxiety_words:
                    try:
                        if text_list[j-1] == '[':
                            mood_matrix[7] = mood_matrix[7] + 3
                    except:
                        pass
                    mood_matrix[7] = mood_matrix[7] + 1

            Max = max(mood_matrix)
            g = mood_matrix.index(Max) #返回情绪值最高的索引
            if Max in (mood_matrix[:g]+mood_matrix[g+1:]):#若含有2个最高值，则该情绪定义为其他
                text_mood = 8
            else:
                text_mood = g
            user_mood[text_mood] += 1 #在对应的情绪值加一

        user_mood.pop() #除去'其他'的情绪值
        M = max(user_mood)
        g = user_mood.index(M)
        if (M==0)|(M in (user_mood[:g]+user_mood[g+1:])):#若情绪值最大值为0,或者有2个最大的情绪值,则规定该用户该日的情绪为'其他'
            return 8
        else:
            return g

    def __start(self):
        start = time.time()
        print "开始分析用户的情绪..."
        d = 1
        for i in User.IDs:
            User.Dict[i].setMood(self.__userMoodAnalyze(User.Dict[i].getBlog()))
            print "   分析中...%i%%"%((d/float(User.Num))*100),
            sys.stdout.write('\r')
            d += 1
        end = time.time()
        print '所有用户情绪分析完成,花费时间:' , end-start,'s'