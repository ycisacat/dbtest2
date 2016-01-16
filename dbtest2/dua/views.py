# coding=utf-8
import json

from django.shortcuts import render, render_to_response
from django import forms
from django.contrib.auth import authenticate as au, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.template.context import RequestContext

from sina.class_mysql_uid import *
from sina.class_page import *
from sina.temp.exercise import *
from sina.draw.draw_alljs import *

# json:dump(s)--把xx打包为json,load(s)--把json解压为xx;字典类型不能传输



class UserForm(forms.Form):  # 登陆页面用户表单
    username = forms.CharField(label='用户名：', error_messages={'required': '请输入用户名'}, max_length=50)
    password = forms.CharField(label='密码：', error_messages={'required': '请输入密码'}, widget=forms.PasswordInput())

def login_page(request):
    if request.user.is_authenticated():
        return render_to_response('nanguo.html', RequestContext(request, {'existed': True}))
    if request.method == "POST":
        uf = UserForm(request.POST)
        try:
            uf.is_valid()
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            user = au(username=username, password=password)

            if user is not None:  # au:如果正确返回User对象,否则返回None
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/main_page/%s' % user.username)
            else:
                return render_to_response('home.html', {'wrong': True})
        except Exception, e:  # 某一项为空都会转到这里
            print e
            # return render_to_response('login.html', RequestContext(request, {'wrong': True}))
    else:  # 非登录用户会到回到登录页
        return render_to_response('manyi.html')

class RegisterForm(forms.Form):
    # email=forms.EmailField(max_length=50,label='邮箱',error_messages={'required':'请输入邮箱'})
    name_1 = forms.CharField(max_length=50, label='用户名', error_messages={'required': '请输入用户名'})
    pwd_1 = forms.CharField(max_length=50, label='密码', error_messages={'required': '请输入密码'})

def register_page(request):  # 9.2:js2可以连接到这个函数,表单名pwd3,pwd2这些修改无效,只能跟着js命名
    if request.method == 'POST':  # 当提交表单时
        print request
        rf = RegisterForm(request.POST)  # rf 包含提交的数据
        try:

            a = rf.is_valid()   # 如果提交的数据合法
            name_1 = rf.cleaned_data['name_1']
            pwd_1 = rf.cleaned_data['pwd_1']

            tmp = MyUser.objects.exclude(pk=request.user.pk)
            # if tmp.filter(email=email).exists(): #
            #     return render_to_response('register.html',RequestContext(request,{'registered_email':True}))
            if tmp.filter(name=name_1).exists():  # 用户名判重
                return render_to_response('jingya.html', RequestContext(request, {'registered_name': True}))
            else:
                MyUser.objects.create(name=name_1, password=pwd_1)
            return HttpResponseRedirect('/buman/')
        except (ValueError, KeyError), e:
            print e
            return render_to_response('errors.html', RequestContext(request, {'registered': True}))
    else:
        rf = RegisterForm()  # 当正常访问时
        return render_to_response('home.html')# RequestContext(request, {'existed': False}))


def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/login')


def main_page(request):
    draw_all()
    return render(request, 'index.html')

class GetId(forms.Form):
    number = forms.CharField(label='编号(0-1)')

def get_id(request):
    db = Database()
    user_list = db.get_mysql_user(1, 20)
    dict_uid = dict()
    dict_uid['user_id'] = user_list
    post_data = json.dumps(dict_uid)
    pc = Page()
    pc.getId(post_data)

    return HttpResponse(post_data)


def kaixin(request):
    # drawLine('/home/yc/PycharmProjects/dbtest2/static/js/test2.js')
    return render(request, 'kaixin.html')


def kuaile(request):
    string = u'Welcome to mysite!!'
    TutorialList = ["HTML", "CSS", "jQuery", "Python", "Django"]
    info_dict = {'label': u'键', 'content': u'值'}
    return render(request, 'kuaile.html', {'info_dict': info_dict})


def manyi(request):
    List = ['jian','zhi']
    Dict = {'a':'jian','b':'zhi'}

    return render(request, 'manyi.html',{
        'list':json.dumps(List),
        'Dict':json.dumps(Dict)
    })



def tonghen(request):
    List = ['自强学堂', '渲染Json到模板']
    Dict = {'site': '自强学堂', 'author': '涂伟忠'}
    return render(request, 'tonghen.html', {
            'List': json.dumps(List),
            'Dict': json.dumps(Dict)
        })
    # return render(request, 'tonghen.html')


def jingya(request):
    account=bbb(1,2)
    return render(request, 'jingya.html',{'list':account})


def wunai(request):
    return render(request, 'jingya.html')


def nanguo(request):
    return render(request, 'nanguo.html')


def buman(request):
    return render(request, 'buman.html')
