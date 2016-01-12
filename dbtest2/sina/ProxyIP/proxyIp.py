# -*- coding: utf-8 -*-
__author__ = 'K'

import urllib2
import random
import time
import re

def getIpFromYDL():
    # setIpProxy(getIpInFile())    #设置代理
    headers = {
        'Accept':"text/css,*/*;q=0.1",
        'Connection':"keep-alive",
        'Host':"www.youdaili.net",
        'User-Agent':"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:41.0) Gecko/20100101 Firefox/41.0"
    }
    req1 = urllib2.Request(
        url = 'http://www.youdaili.net/Daili/',
        headers = headers
    )

    proxyTypeDict = {'chinaProxy' : "【国内代理】" , 'foreignProxy' : "【国外代理】" }  # 可添加  'socksProxy' : "【Socks代理】" ,'httpProxy' : "【HTTP代理】"
    proxyTypeUrlDict = {}
    try :
        req = urllib2.urlopen(req1,timeout=20)
        respon = req.read()
        # print respon
        # for key in proxyTypeDict.keys():
        pattern = '<li><a href="(.*?)" target="_blank"><font color=#FF7300>'+proxyTypeDict['chinaProxy']+'</font>'
        url = re.search(pattern,respon).group(1)
        proxyTypeUrlDict.setdefault('chinaProxy',url)
    except Exception,e:   #有些代理不能用导致异常，返回0表示失败
        print e
        return 0
    # for proxyType in proxyTypeUrlDict.keys():
    YDL('chinaProxy',proxyTypeUrlDict['chinaProxy'])
    print 'YDL finish'
    # time.sleep(2)
    return 1

def YDL(proxyType,url):
    proxyList = []
    stateList = []
    headers = {
        'Accept':"text/css,*/*;q=0.1",
        'Connection':"keep-alive",
        'Host':"www.youdaili.net",
        'Referer':"http://www.youdaili.net/Daili/",
       'User-Agent':"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:41.0) Gecko/20100101 Firefox/41.0"
    }
    pattern = '<div class="cont_font">[\w\W]+?<p>([\w\W]+?)</p>'
    tempUrl = url.replace('.html','')
    number = 1
    pageLen = 1
    count=0
    while True:
        print "looping"
        if number > pageLen:
            break
        if number == 1:
            url = tempUrl + '.html'
        else:
            url = tempUrl+"_"+str(number)+".html"
        print url
        count+=1
        if count ==2:
            break
        try:
            req1=urllib2.Request(
                url = url,
                headers = headers
            )
            req = urllib2.urlopen(req1,timeout=8)
            respon = req.read()
            # print 'respond',respon
            list=re.search(pattern,respon).group(1).split("<br />")
        except Exception,e:
            print proxyType,"Error! ",e
            setIpProxy(getIpInFile())
            time.sleep(20)
            continue
        '''
        if number == 1: #此代码可不要，要了之后，将爬取第二页以后的代理，第二页后的代理不知道是否有效。
            try:
                pageLen = int(re.search('共([\d]+)页: ',respon).group(1))
            except:
                pass
        time.sleep(20)
        '''
        number = number + 1
        for temp in list:
            try:
                ip = temp.split("#")
                stateList.append(ip[1])
                ip = ip[0].split('@')
                if ip[1] == 'HTTP':
                    proxyList.append({'http': 'http://'+ip[0].replace("\r\n",'')})
                elif ip[1] == "HTTPS":
                    proxyList.append({'https': 'https://'+ip[0]})
                else:
                    pass
            except:
                pass
    fileProxyIp = open('./proxyIp/'+proxyType+'Ip.txt','w')
    for i in range(len(proxyList)):
        fileProxyIp.write(stateList[i]+'#')
        temp = proxyList[i]
        fileProxyIp.write(str(temp))
        fileProxyIp.write('\r\n')
    fileProxyIp.flush()
    fileProxyIp.close()
    print proxyType,len(proxyList),"finish!"


def setIpProxy(ipProxyList):   #设置代理
    ipProxy = ipProxyList[random.randint(0, len(ipProxyList) - 1)]
    proxy_support = urllib2.ProxyHandler(ipProxy)
    opener = urllib2.build_opener(proxy_support, urllib2.HTTPHandler)
    urllib2.install_opener(opener)

def clearIpProxy(): #清除代理
     urllib2.install_opener(None)

def getIpInFile():  #从txt文件中读取代理
    file=open("ip.txt",'r')
    ipProxyList=[]
    while True:
        temp=file.readline()
        if temp:
            ipProxyList.append(eval(temp))
        else:
            break
    return ipProxyList

def getProxyIp(fileName):  #chinaProxyIp 或 foreignProxyIp
    file=open("./proxyIp/"+fileName+".txt",'r')
    ipProxyList = []
    while True:
        temp = file.readline()
        if temp != '':
            temp = temp.split("#")[1]
            ipProxyList.append(eval(temp))
        else:
            break
    return ipProxyList

def saveAliveIp(fileName):
    print 'saveAliveIp'
    ipProxyList = getProxyIp(fileName)
    newIpProxyList = []
    for i in range(0,len(ipProxyList)):
        if testIp(ipProxyList[i]):
            newIpProxyList.append(ipProxyList[i])
        time.sleep(1)

    fileIp = open('ip.txt','w+')
    for ipProxy in newIpProxyList:
        fileIp.write(str(ipProxy)+'\r\n')   #更新ip.txt
    fileIp.flush()
    fileIp.close()



def testIp(ipProxy):    #测试代理是否有效
    print "testIp"
    proxy_support = urllib2.ProxyHandler(ipProxy)
    opener = urllib2.build_opener(proxy_support, urllib2.HTTPHandler)
    urllib2.install_opener(opener)

    try:
        req = urllib2.urlopen('http://www.baidu.com/',timeout=8)
        req.read()
    except Exception,e:
        print e
        return False
    return True


def getProxyIpControl():
    print 'getProxyIpControl'
    flag = 0
    while flag == 0:
        flag = getIpFromYDL()
    saveAliveIp('chinaProxyIp')


