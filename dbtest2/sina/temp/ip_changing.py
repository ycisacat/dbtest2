#coding=utf-8
#!/usr/bin/python
# -*- coding: utf-8 -*-
import socket
import random
import netifaces as ni
import random
true_socket = socket.socket
ipList=[('14.18.234.160:8080','14.29.116.15:80'),('27.221.10.194:8081','42.121.33.160:8080'),('42.121.105.155:8888',
'58.19.115.96:80'),'58.30.233.196:80']
print ipList[random.randint(1,len(ipList)-1)]


class BindIp():
    ip=''
    global true_socket,ipList
    def getLocalEthIps(self):
        for dev in ni.interfaces():
            if dev.startswith('eth0'):
                ip=ni.ifaddresses(dev)[2][0]['addr']
                if ip not in ipList:
                    ipList.append(ip)

    def bound_socket(self,*a, **k):
        sock = true_socket(*a, **k)
        sock.bind((self.ip, 0))
        return sock

    def changeIp(self,ipaddress):
        self.ip=ipaddress
        if not self.ip=='':
            socket.socket = self.bound_socket
        else:
            socket.socket = true_socket
        return socket.socket

    def randomIp(self):
        if len(ipList)==0:
            return
        _ip=random.choice(ipList)
        if not _ip==self.ip:
            self.changeIp(_ip)

    def getIp(self):
        return self.ip

    def getIpsCount(self):
        return len(ipList)


