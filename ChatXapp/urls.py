from django.contrib import admin
from django.urls import path,include
from ChatXapp.views import *

urlpatterns = [
    path('',index,name="home"),
    path('<str:username>/',chatPage,name="chat"),

]
