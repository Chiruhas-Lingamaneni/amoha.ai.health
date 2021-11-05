from django.contrib import admin
from django.urls import path,include
from home import views

app_name='home'

urlpatterns = [
    path('signin/',views.register,name='register'),
    path('login/',views.userlogin,name='login'),
    path('userdetail/',views.logedin,name='userdetail'),
    path('logedout/',views.logedout,name='logedout'),
    path('uploadimg',views.uploadimg,name='uploadimg'),
    path('query',views.getintouch,name='query'),
]