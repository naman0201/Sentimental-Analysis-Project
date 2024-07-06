from django import urls
from django.urls import path
from django.urls.conf import include
from . import views



urlpatterns = [
    path('', views.index, name="indexview"),
    path('login',views.loginuser,name="login_user"),
    path('register',views.registeruser,name="register_user"),
    path('logout',views.logoutuser,name="logout_user"),
]
