from django.shortcuts import render

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