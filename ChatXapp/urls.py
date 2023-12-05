from django.contrib import admin
from django.urls import path,include
from ChatXapp.views import *

urlpatterns = [
    path('',index,name="home"),
    path('chat/<str:username>/',chatPage,name="chat"),
    path('rooms/',rooms,name="rooms"),
    path('<slug:slug>/',room,name="room"),

]
