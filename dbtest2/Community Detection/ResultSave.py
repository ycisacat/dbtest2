#coding=utf-8
'''
Author = Eric_Chan
Create_Time = 2016/1/15
'''
'''
This py is used to save the result of the community detection.
There are have 8 communities.(0:'disgust',1:'sympathy',2:'like',3:'hate',4:'sad',5:'happy',6:'angry',7:'anxiety')
The result include:
    0.the account of each community
    1.all the ids in one community
    2.the value of mood in one community
'''

class DisgustResult:
    def __init__(self):
        self.IDs = []
        self.num = 0
        self.valueOfMood = [0] * 8

    def getIDs(self):
        return self.IDs

    def setIDs(self,IDs):
        self.IDs = IDs

    def setNum(self,num):
        self.num = num

    def getNum(self):
        return self.num

    def setValueOfMood(self,valueOfMood):
        self.valueOfMood = valueOfMood

    def getValueOfMood(self):
        return self.valueOfMood

class SympathyResult:
    def __init__(self):
        self.IDs = []
        self.num = 0
        self.valueOfMood = [0] * 8

    def getIDs(self):
        return self.IDs

    def setIDs(self,IDs):
        self.IDs = IDs

    def setNum(self,num):
        self.num = num

    def getNum(self):
        return self.num

    def setValueOfMood(self,valueOfMood):
        self.valueOfMood = valueOfMood

    def getValueOfMood(self):
        return self.valueOfMood

class LikeResult:
    def __init__(self):
        self.IDs = []
        self.num = 0
        self.valueOfMood = [0] * 8

    def getIDs(self):
        return self.IDs

    def setIDs(self,IDs):
        self.IDs = IDs

    def setNum(self,num):
        self.num = num

    def getNum(self):
        return self.num

    def setValueOfMood(self,valueOfMood):
        self.valueOfMood = valueOfMood

    def getValueOfMood(self):
        return self.valueOfMood

class HateResult:
    def __init__(self):
        self.IDs = []
        self.num = 0
        self.valueOfMood = [0] * 8

    def getIDs(self):
        return self.IDs

    def setIDs(self,IDs):
        self.IDs = IDs

    def setNum(self,num):
        self.num = num

    def getNum(self):
        return self.num

    def setValueOfMood(self,valueOfMood):
        self.valueOfMood = valueOfMood

    def getValueOfMood(self):
        return self.valueOfMood

class SadResult:
    def __init__(self):
        self.IDs = []
        self.num = 0
        self.valueOfMood = [0] * 8

    def getIDs(self):
        return self.IDs

    def setIDs(self,IDs):
        self.IDs = IDs

    def setNum(self,num):
        self.num = num

    def getNum(self):
        return self.num

    def setValueOfMood(self,valueOfMood):
        self.valueOfMood = valueOfMood

    def getValueOfMood(self):
        return self.valueOfMood

class HappyResult:
    def __init__(self):
        self.IDs = []
        self.num = 0
        self.valueOfMood = [0] * 8

    def getIDs(self):
        return self.IDs

    def setIDs(self,IDs):
        self.IDs = IDs

    def setNum(self,num):
        self.num = num

    def getNum(self):
        return self.num

    def setValueOfMood(self,valueOfMood):
        self.valueOfMood = valueOfMood

    def getValueOfMood(self):
        return self.valueOfMood

class AngryResult:
    def __init__(self):
        self.IDs = []
        self.num = 0
        self.valueOfMood = [0] * 8

    def getIDs(self):
        return self.IDs

    def setIDs(self,IDs):
        self.IDs = IDs

    def setNum(self,num):
        self.num = num

    def getNum(self):
        return self.num

    def setValueOfMood(self,valueOfMood):
        self.valueOfMood = valueOfMood

    def getValueOfMood(self):
        return self.valueOfMood

class AnxietyResult:
    def __init__(self):
        self.IDs = []
        self.num = 0
        self.valueOfMood = [0] * 8

    def getIDs(self):
        return self.IDs

    def setIDs(self,IDs):
        self.IDs = IDs

    def setNum(self,num):
        self.num = num

    def getNum(self):
        return self.num

    def setValueOfMood(self,valueOfMood):
        self.valueOfMood = valueOfMood

    def getValueOfMood(self):
        return self.valueOfMood
