#coding=utf-8
import urllib
import base64
import rsa
import binascii


def PostEncode(userName,passWord,serverTime,nonce,pubkey,rsakv):
    encodedUserName=GetUserName(userName)
    encodedPassWord=GetPwd(passWord,serverTime,nonce,pubkey)
    postPara={
        'entry': 'weibo',
        'gateway': '1',
        'from': '',
        'savestate': '7',
        'userticket': '1',
        'ssosimplelogin': '1',
        'vsnf': '1',
        'vsnval': '',
        'su': encodedUserName,
        'service': 'miniblog',
        'servertime': serverTime,
        'nonce': nonce,
        'pwencode': 'rsa2',
        'sp': encodedPassWord,
        'encoding': 'UTF-8',
        'prelt': '115',
        'rsakv': rsakv,
        'url': 'http://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack',
        'returntype': 'META'
    }
    postData=urllib.urlencode(postPara)
    return postData

def GetUserName(userName):
    userNameTemp=urllib.quote(userName)
    userNameEncoded=base64.encodestring(userNameTemp)[:-1]
    return userNameEncoded

def GetPwd(passWord,serverTime,nonce,pubkey): #用于rsa加密的密码
    rsaPublickey=int(pubkey,16)
    key=rsa.PublicKey(rsaPublickey,65537)#创建公钥
    message=str(serverTime)+'\t'+str(nonce)+'\n'+str(passWord) #拼接明文js加密文件
    pwd=rsa.encrypt(message,key) #加密
    pwd=binascii.b2a_hex(pwd)
    return pwd
