#coding=utf-8
__author__ = 'yc'
def show_database(request, id):
    try:
        user = SinaUser.objects.get(pk=id)
        fans = GDFan.objects.order_by('gdfans_id')
        follows = GDFollow.objects.order_by('gdfollows_id')
        weibo = WeiboText.objects.order_by('time')
        content = {'user': user, 'fans': fans, 'follows': follows, 'weibo': weibo}
    except:
        raise Http404("Question does not exist")
    return render_to_response('showdb.html', content)

def index(request):
    if request.user.is_authenticated():
        return render_to_response('index.html', RequestContext(request, {'success': True}))
    else:
        return render_to_response('index.html', {'success': False})

def main_page(request):
    if request.user.is_authenticated():
        return render_to_response('main_page.html', RequestContext(request,{'existed':True}))
    if request.method == "POST":
        uf = UserForm(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            user = au(username=username, password=password)
            if user is not None:  #au:如果正确返回User对象,否则返回None
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/main_page/%s' % user.username)
            else:
                    return render_to_response('login.html',{'wrong':True})
        else: #某一项为空都会转到这里
            return render_to_response('login.html', RequestContext(request, {'wrong': True}))
    else:
        return HttpResponseRedirect('main_page.html')