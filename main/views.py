from enum import Flag
from django.db.models import base
from django.shortcuts import render
from .models import Userss
# Create your views here.


def setCookie(request):
    response =  render(request,'main/setcookie.html')
    response.set_cookie('name','kamran')
    return response

def getcookie(request):
    # try:
    #     name = request.COOKIES['name']
    #     print(name)
    #     return render(request,'main/getcookie.html',{'name':name})
    # except:
    #     return render(request,'main/getcookie.html')

    # or 

    name = request.COOKIES.get('name','GUEST')
    return render(request,'main/getcookie.html',{'name':name})


def deletecookie(request):
    response = render(request,'main/deletecookie.html')
    response.delete_cookie('name')

    return response

def signup(request):
    flag=1
    context = {'status':flag}
    return render(request,'main/signup.html',context)

def addnew(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        newdata = Userss(username=username,password=password)
        newdata.save()
        stats='User signed up'
        context={'status':stats}
    else:
        stats='Not Signed up || Logged in'
        context={'status':stats}
    return render(request,'main/signup.html',context)
