#coding=utf-8
# Create your views here.
from django.shortcuts import render_to_response
from login.models import User
from django.http import HttpResponseRedirect
from django import forms
from django.template.context import RequestContext

#定义表单类型
class UserForm(forms.Form):
    username = forms.CharField(label='账号：',max_length=100)
    password = forms.CharField(label='密码：',widget=forms.PasswordInput)

def login(request):
    if request.method == 'POST':
        uf = UserForm(request.POST) 
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            user = User.objects.filter(username__exact = username,password__exact=password) 
            if user:
                request.session['username'] = username
                return render_to_response('success.html',{'username':username})
            else:
                return HttpResponseRedirect('/login/')
    else:
        uf = UserForm()
    return render_to_response('login.html',{'uf':uf})

def register(request):
    if request.method =='POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            user = User.objects.filter(username__exact = username,password__exact=password)
            if user:
                return HttpResponseRedirect('/login/register/')
            else:
                User.objects.create(username= username,password=password)
                return render_to_response('registersucc.html',{'username':username})
    else:
        uf = UserForm()
    return render_to_response('register.html',{'uf':uf},context_instance = RequestContext(request)) 

def logout(request):
    del request.session['username']
    return HttpResponseRedirect('/login/login/')