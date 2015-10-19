#coding=utf-8
import urllib2
import cookielib

from sinalogin import encodetest1, searchtest1


class WeiboLogin:
    def __init__(self,user,pwd,enableProxy=False):
        print "Initializing login"
        self.userName=user
        self.passWord=pwd
        self.enableProxy=enableProxy
        self.serverUrl="http://login.sina.com.cn/sso/prelogin.php?entry=account&callback=sinaSSOController.preloginCallBack&su=NzA3MDU0MjB5YyU0MHNpbmEuY29t&rsakt=mod&client=ssologin.js(v1.4.15)&_=1438087270766"
        self.loginUrl="https://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.15)" #&_=1438087270929"
        self.postHeader={'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0'}
    def Login(self):
        self.EnableCookie(self.enableProxy)
        serverTime,nonce,pubkey,rsakv=self.GetServerTime()
        postData= encodetest1.PostEncode(self.userName,self.passWord,serverTime,nonce,pubkey,rsakv)
        print "post data length:",len(postData)
        req=urllib2.Request(self.loginUrl,postData,self.postHeader)
        print "post request"
        result=urllib2.urlopen(req)
        text=result.read()
        try:
            loginUrl= searchtest1.sRedirectData(text)
            urllib2.urlopen(loginUrl)
        except:
            print "Login error"
            return False
        print "Login success"
        return True
    def EnableCookie(self,enableProxy):
        cookiejar=cookielib.LWPCookieJar() #建立cookie
        cookie_support=urllib2.HTTPCookieProcessor(cookiejar)
        if enableProxy:
            proxy_support=urllib2.ProxyHandler({'http':'http://xxxxx.pac'})
            opener=urllib2.build_opener(cookie_support,urllib2.HTTPHandler)
            print "Proxy enabled"
        else:
            opener=urllib2.build_opener(cookie_support,urllib2.HTTPHandler)
        urllib2.install_opener(opener)
    def GetServerTime(self):
        print "Get server time and nonce"
        serverData=urllib2.urlopen(self.serverUrl).read()
        print serverData
        try:
            serverTime,nonce,pubkey,rsakv= searchtest1.sServerData(serverData) #解析得到servertime等
            return serverTime,nonce,pubkey,rsakv
        except:
            print "error"
            return None
    # def SaveCookie():   #记住登录状态
    #
    # return opener
if __name__=='__main__':
    weiboLogin=WeiboLogin('70705420yc@sina.com','1234567')
    if weiboLogin.Login()==True:
        print "success"