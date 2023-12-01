from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path,include
from .views import *

urlpatterns = [
   
    path("signup/",signup,name='signup'),
    path("logout/",auth_views.LogoutView.as_view(),name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='register/login.html'), name='login'),

]