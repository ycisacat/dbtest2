#coding=utf-8
'''
Author = Eric_Chan
Create_Time = 2015/12/5
'''
'''
输入:社区检测结果
输出:8大情绪社区,并将各社区的人数,情绪值,用户ID保存
'''

from WeiboUser import *
from ResultSave import *

class CommunityIdentification():
    def __init__(self,divisionResult):
        self.divisionResult = divisionResult
        self.moodDict = {0:'disgust',1:'sympathy',2:'like',3:'hate',4:'sad',5:'happy',6:'angry',7:'anxiety'}
        self.identificating()

    def __identificateMoodOfCommunity(self,community):#input a community and output the mood and the value of the mood in this community
        valueOfMood = [0]*8 #record the value of 8 moods
        for SY in community:
            try:
                valueOfMood[User.Dict[User.IDs[SY]].getMood()] += 1
            except:
                continue
        return valueOfMood.index(max(valueOfMood)) , valueOfMood

    def identificating(self):

        userNumOfCommunity = [0] * 8
        for community in self.divisionResult: #ignore the community which's the number is below 10
            if len(community)<10:
                continue
            else:
                numMoodOfCommunity , valueOfMood = self.__identificateMoodOfCommunity(community)
                if userNumOfCommunity[numMoodOfCommunity] > len(community):
                    continue
                else:
                    userNumOfCommunity[numMoodOfCommunity] = len(community)

                    # #result output txt
                    # newFileName = "result/CommunityIdentification/%s.txt"%self.moodDict[numMoodOfCommunity]
                    # f = open(newFileName,'w')
                    # for SY in community:
                    #     f.write(str(User.IDs[SY])+'\n')
                    # f.close()

                    #write result into class
                    IDs = []
                    for SY in community:
                        IDs.append(User.IDs[SY])
                    if numMoodOfCommunity == 0:
                        MoodResult = DisgustResult
                    elif numMoodOfCommunity == 1:
                        MoodResult = SympathyResult
                    elif numMoodOfCommunity == 2:
                        MoodResult = LikeResult
                    elif numMoodOfCommunity == 3:
                        MoodResult = HateResult
                    elif numMoodOfCommunity == 4:
                        MoodResult = SadResult
                    elif numMoodOfCommunity == 5:
                        MoodResult = HappyResult
                    elif numMoodOfCommunity == 6:
                        MoodResult = AngryResult
                    elif numMoodOfCommunity == 7:
                        MoodResult = AnxietyResult
                    MoodResult().setIDs(IDs = IDs)
                    MoodResult().setNum(len(community))
                    MoodResult().setValueOfMood(valueOfMood=valueOfMood)

