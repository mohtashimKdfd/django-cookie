
from django.shortcuts import render
from .models import Userss
# Create your views here.
flag=0


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
    response = render(request,'main/logout.html')
    response.delete_cookie('name')

    return response

def signup(request):
    name = request.COOKIES.get('name','GUEST')
    if name and name != 'GUEST':
        return render(request,'main/signup.html',{'status':'User already signed in'})
    context = {'status':'Not signed'}
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

def login(request):
    return render(request,'main/login.html')

def authenticate(request):
    if request.method=='POST':
        username = request.POST.get('username')
        if Userss.objects.filter(username=username).exists():
            targetuser = Userss.objects.get(username=username)
            print(targetuser,targetuser.password)
            if request.POST.get('password')==targetuser.password:
                response = render(request,'main/login.html',{'status':'Logged in'})
                response.set_cookie('name',username)
                global flag
                flag=1
                return response
            else:
                return render(request,'main/login.html',{'status':"Error Password"})
        else:
            return render(request,'main/login.html',{'status':'no user exist||Signup'})
    return render(request,'main/login.html',{'status',''})
