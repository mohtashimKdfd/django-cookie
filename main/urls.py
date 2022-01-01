from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('register',views.setCookie,name='setcookie'),
    path('getcook',views.getcookie,name='getcookie'),
    path('delete',views.deletecookie,name='delete cookie'),
    path('signup',views.signup,name='signup'),
    path('addnew',views.addnew,name='addnew')
]