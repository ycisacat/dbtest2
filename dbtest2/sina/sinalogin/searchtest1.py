#coding=utf-8
import re,json
#解释从服务器得到的数据
def sServerData(serverData):
    p=re.compile('\((.*)\)')
    jsonData=p.search(serverData).group(1)
    data=json.loads(jsonData)
    serverTime=str(data['servertime'])
    nonce=data['nonce']
    pubkey=data['pubkey']
    rsakv=data['rsakv']
    print "servertime",serverTime,"nonce",nonce
    return serverTime,nonce,pubkey,rsakv

def sRedirectData(text):
    p=re.compile('location\.replace\([\'"](.*?)[\'"]\)')
    loginUrl=p.search(text).group(1)
    print "loginurl",loginUrl
    return loginUrl
