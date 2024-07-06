from django.http import HttpResponse
from django.shortcuts import render,redirect
from random import randint
import re
## user works
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth import login as auth_login

# API works
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from ProjectHome.models import webUser
from .serializers import RegisterSerializer,LoginSerializer
# from TSA.ProjectHome.api import serializers



def index(request):
    return HttpResponse("This is index view!")

@api_view(["POST",])
def loginuser(request):
    serializer = LoginSerializer(data=request.data)
    data={}
    if serializer.is_valid():
        loginusername = serializer.validated_data['email']
        loginpassword = serializer.validated_data['password']
        try:
            if valiemail(loginusername):
                email1 = User.objects.filter(email=loginusername)
                user=authenticate(username= email1[0], password= loginpassword)
            else:
                user=authenticate(username= loginusername, password= loginpassword)
            if user is not None:
                auth_login(request, user)
                data['status']="200" # success protocol
                data['message'] = "Successfully Logged in"
            else:
                data['status']="420" # success protocol
                data['message'] = "Invalid credentials! Please try again"
        except:
            data['status']="420" # success protocol
            data["message"] = "Invalid credentials! Please try again"
    return Response(data)        
    
@api_view(["POST",])
def registeruser(request):
    serializer = RegisterSerializer(data=request.data)
    data ={}
    if serializer.is_valid():
        email = serializer.validated_data['email']
        name = serializer.validated_data['name']
        password1 = serializer.validated_data['password']
        password2 = serializer.validated_data['password2']
        if len(email) > 200:
                data['message'] = " Your email must be under 200 characters"
                data['status']="420" # success protocol
                return redirect('/api/register')
        if (password1!= password2):
            data['message'] = "passwords does not match !"
            data['status']="420" # success protocol
            return redirect('/api/register')
        username = 'U'+ email[:3]+str(random_with_N_digits((len(email)%5)+1))
        myuser = User.objects.create_user(username, email, password1)
        myuser.save()
        webUser.objects.create(email=email,name=name,password=password1,Susername=username,user=myuser)
        data['message'] = "successfully registered a new user."
        data['status']="200" # success protocol
    else:
        data = serializer.errors
    return Response(data)

def logoutuser(request):
    try:
        logout(request)
        return redirect('/')
    except:
        return HttpResponse("There is some error at server please try again later !")





def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)



def valiemail(emailva):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.fullmatch(regex, emailva)