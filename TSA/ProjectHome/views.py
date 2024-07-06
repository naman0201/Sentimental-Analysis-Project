from ProjectHome.api.serializers import RegistrationwebuserSerializer
from .serializers import webuserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ProjectHome.models import webUser
from pandas.core.common import random_state
from urllib import response
from django.shortcuts import render, redirect
from django.db.models.fields import AutoField
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import login as auth_login
# importing the modules to be used in backend
from bs4 import BeautifulSoup as bs
import requests
import re
# Import the libraries for
import tweepy
from textblob import TextBlob
# from wordcloud import WordCloud
import pandas as pd
import numpy as np
import os
import os.path
from pathlib import Path
from random import randint
# import WordCloud
import matplotlib.pyplot as plt


plt.style.use("fivethirtyeight")

# API works


@api_view(['GET'])
def getData(request):
    person = webUser.objects.all()
    serilizer = webuserSerializer(person, many=True)
    return Response(serilizer.data)


@api_view(['POST'])
def addItem(request):
    serilizef = webuserSerializer(data=request.data)
    print(serilizef)
    if serilizef.is_valid():
        serilizef.save()
    return Response(serilizef.data)


@api_view(['POST', ])
def RegisterUser(request):
    print("POST method se before ! ")
    # if request.method == 'POST':
    serializer = RegistrationwebuserSerializer(data=request.data)
    data = {}
    print("before saving the valid function ! ")
    print("serializer : ", serializer)
    if serializer.is_valid():
        print("saving the valid ! ")
        serializer.save()
        data['response'] = "successfully registered a new user."
        # data['email'] = webus.email
        # data['username'] = webus.Susername
    else:
        data = serializer.errors
    return Response(data)


# Create your views here.
def index(request):
    return render(request, "ProjectHome\index.html")


def striphtml(data):
    p = re.compile(r'<.*?>')
    return p.sub('', data)


def DataPage(request):
    # try:
    # if request.method == "POST":
        # Ecommercesite = request.POST.get("EcommerceSite")
        # ProductName = request.POST.get('Productname')
        # Productlink = request.POST.get('linkofproduct')
        heading = ["No values"]
        content = ["No values"]
        link = ""
        Ecommercesite = "Flipkart"
        ProductName = "Television"
        Productlink = "https://www.flipkart.com/oneplus-u1s-164-cm-65-inch-ultra-hd-4k-led-smart-android-tv/p/itm8625fe03919f2?pid=TVSG3E9A3MNZUTQK&lid=LSTTVSG3E9A3MNZUTQK973KNU&marketplace=FLIPKART&fm=neo%2Fmerchandising&iid=M_61b74cb7-b40c-4f32-a55e-21cfc4b556fb_7_QX0K9XF6VS46_MC.TVSG3E9A3MNZUTQK&ppt=clp&ppn=infinixdaysmay22-store&ssid=lclydptqa80000001652122963229&otracker=clp_pmu_v2_Large%2BScreen%2BTVs_1_7.productCard.PMU_V2_OnePlus%2BU1S%2B164%2Bcm%2B%252865%2Binch%2529%2BUltra%2BHD%2B%25284K%2529%2BLED%2BSmart%2BAndroid%2BTV_television-store_TVSG3E9A3MNZUTQK_neo%2Fmerchandising_0&otracker1=clp_pmu_v2_PINNED_neo%2Fmerchandising_Large%2BScreen%2BTVs_LIST_productCard_cc_1_NA_view-all&cid=TVSG3E9A3MNZUTQK"
        
        # link = 'https://www.flipkart.com/realme-9-5g-stargaze-white-64-gb/p/itm4f3814d50ff53?pid=MOBGC2Q5HG5RJZGW&lid=LSTMOBGC2Q5HG5RJZGWWUP6TT&marketplace=FLIPKART&store=tyy%2F4io&srno=b_1_10&otracker=clp_metro_expandable_1_3.metroExpandable.METRO_EXPANDABLE_Shop%2BNow_mobile-phones-store_Q1PDG4YW86MF_wp3&fm=neo%2Fmerchandising&iid=62a354e1-c0a1-4241-847e-161dc8e17677.MOBGC2Q5HG5RJZGW.SEARCH&ppt=clp&ppn=mobile-phones-store&ssid=en1ht3svk00000001648989371787'
        # link= 'https://www.snapdeal.com/product/veirdo-green-half-sleeve-tshirt/639827458615'
        # link = 'https://www.myntra.com/jeans/roadster/roadster-men-navy-blue-skinny-fit-mid-rise-clean-look-stretchable-jeans/11274548/buy'
        page = requests.get(Productlink)
        print("request error is : ", page)
        soup = bs(page.content, 'html.parser')

        if Ecommercesite == "Amazon":
            heading = soup.find_all('p', class_='_2-N8zT')
            content = soup.find_all('div', class_='t-ZTKy')
        elif Ecommercesite == "Flipkart":
            heading = soup.find_all('p', class_='_2-N8zT')
            content = soup.find_all('div', class_='t-ZTKy')
        elif Ecommercesite == "Meshow":
            pass
        elif Ecommercesite == "Myntra":
            # heading = soup.find_all('p',class_='_2-N8zT')
            content = soup.find_all(
                'div', class_='user-review-reviewTextWrapper')
            # print(content)
        elif Ecommercesite == "Shopee":
            pass
        elif Ecommercesite == "Snapdeal":
            names = soup.find_all('span', class_='_reviewUserName')
            # print(names)
            review = soup.find_all('div', class_='commentlist')
            # print(review)
        elif Ecommercesite == "Too Good":
            pass
        elif Ecommercesite == "Zivame":
            pass
        heading = [ik for ik in heading]
        heading = [striphtml(str(ik)) for ik in heading]
        emty = [ik for ik in content]
        poi = [striphtml(str(ik)) for ik in emty]
        content = poi
        allcont = zip(heading, content)
        # os.remove("H:\\minor project\\Sentiment analysis Project\\TSA\\static\\Json_Files\\preprocess.json")
        global pd
        df1 = pd.DataFrame(poi, columns=['Text'])
        # print(df1.head())

        df1.to_json("static/Json_Files/preprocess.json")

        params = {'Ecommerecesite': Ecommercesite, "product": ProductName, 'Heading': heading, 'Lengthofheading': range(
            1, len(heading)), 'Content': content, 'allcont': allcont, 'lencount': len(heading)}

        return render(request, "ProjectHome\DataPage.html", params)

    # return render(request, "ProjectHome\InputPage.html", {})
    # except :
    # return render(request,"Errorpage.html",{})


# clean the text

# create  a function to clean the tweets
def cleanTxt(text):
    text = re.sub(r'@[A-Za-z0-9]+', '', text)  # remove @mentions
    text = re.sub(r"#", '', text)  # removing the # symbol
    text = re.sub(r'RT[\s]', '', text)  # removing RT
    text = re.sub(r"https?:\/\/\s+", '', text)  # removing the hyperlink

    return text
# create a functon to get the subjectivitiy


def getSubjectivity(text):
    return TextBlob(text).sentiment.subjectivity

# create a function to get the polarity


def getPolarity(text):
    return TextBlob(text).sentiment.polarity

# create a function to compute the negative ,neutral and positive analysis


def getAnalysis(score):
    if score < 0:
        return 'Negative'
    elif score == 0:
        return 'Neutral'
    else:
        return 'Positive'


def datavisulization(request):
    df_short = pd.read_json('static\Json_Files\preprocess.json')
    if os.path.isfile("H:\\minor project\\Sentiment analysis Project\\TSA\static\\images\\textimage1.png") and os.path.isfile("H:\\minor project\\Sentiment analysis Project\\TSA\\static\\images\\Sentiment_Count_histogram.png") and os.path.isfile("H:\\minor project\\Sentiment analysis Project\\TSA\\static\\images\\ploSubCurve.png"):
        os.remove(
            r"H:\\minor project\\Sentiment analysis Project\\TSA\static\\images\\textimage1.png")
        os.remove(
            r"H:\\minor project\\Sentiment analysis Project\\TSA\\static\\images\\Sentiment_Count_histogram.png")
        os.remove(
            r"H:\\minor project\\Sentiment analysis Project\\TSA\\static\\images\\ploSubCurve.png")
    # cleaning the test =
    df_short['Text'] = df_short['Text'].apply(cleanTxt)
    # show the cleaned text
    # create a new columns

    df_short['Subjectivity'] = df_short['Text'].apply(getSubjectivity)
    df_short['Polarity'] = df_short['Text'].apply(getPolarity)
    # show the data with new columns
    polarity_subjectivity = df_short
    BASE_DIR = Path(__file__).resolve().parent.parent
    TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
    print(BASE_DIR, TEMPLATE_DIR)

    # plotting the word Cloud
    allWords = ' '.join([twts for twts in df_short['Text']])
    # wordcloud = WordCloud(width=500, height=300, random_state=21,
    #                       max_font_size=119).generate(allWords)
    # plt.imshow(wordcloud, interpolation="bilinear")
    # plt.axis('off')
    # plt.savefig("static/images/textimage1.png")
    df_short['Analysis'] = df_short['Polarity'].apply(getAnalysis)
    # show thr datarame
    # print all of the positive tweets
    positive = []
    j = 1
    sortedDF = df_short.sort_values(by=['Polarity'])
    for i in range(0, sortedDF.shape[0]):
        if sortedDF['Analysis'][i] == 'Positive':
            # print(str(j)+')'+sortedDF['Text'][i])
            positive.append(str(j)+')'+sortedDF['Text'][i])
            # print()
            j = j+1
    negative = []
    # print the negative tweets
    j = 1
    sortedDF = df_short.sort_values(by=['Polarity'], ascending=False)
    for i in range(0, sortedDF.shape[0]):
        if sortedDF['Analysis'][i] == 'Negative':
            # print(str(j)+')'+sortedDF['Text'][i])
            # print()
            negative.append(str(j)+')'+sortedDF['Text'][i])
            j = j+1
    neutral = []
    # print the negative tweets
    j = 1
    sortedDF = df_short.sort_values(by=['Polarity'], ascending=False)
    for i in range(0, sortedDF.shape[0]):
        if sortedDF['Analysis'][i] == 'Neural':
            # print(str(j)+')'+sortedDF['Tweets'][i])
            # print()
            negative.append(str(j)+')'+sortedDF['Tweets'][i])
            j = j+1
    # plot the ploarity and subjectivity
    plt.figure(figsize=(8, 6))
    for i in range(0, df_short.shape[0]):
        plt.scatter(df_short['Polarity'][i],
                    df_short['Subjectivity'][i], color="Blue")

    plt.title("Sentiment analysis Plot")
    plt.xlabel('Polarity')
    plt.xlabel('subjectivity')
    # print(plt.show())
    plt.savefig("static/images/ploSubCurve.png")
    print("=======================================================================================================================================")
    # get the percentage of Positive tweets
    ptweets = df_short[df_short.Analysis == "Positive"]
    ptweets = ptweets['Text']

    Posper = (ptweets.shape[0]/df_short['Text'].shape[0])*100
    # print(Posper)
    print("=======================================================================================================================================")
    # get the percentage of Positive tweets
    Ntweets = df_short[df_short.Analysis == "Negative"]
    Ntweets = Ntweets['Text']

    Negper = (Ntweets.shape[0]/df_short['Text'].shape[0])*100
    # print(Negper)
    print("=======================================================================================================================================")
    # get the percentage of Positive tweets
    Neutweets = df_short[df_short.Analysis == "Neutral"]
    Neutweets = Neutweets['Text']

    Neugper = (Neutweets.shape[0]/df_short['Text'].shape[0])*100
    Neugper
    print("=======================================================================================================================================")
    # show the vale conunt
    df_short['Analysis'].value_counts()
    # plot and visulaize the counts
    plt.title("Sentiment analysis")
    plt.xlabel('Sentiment')
    plt.ylabel('Counts')
    df_short['Analysis'].value_counts().plot(kind="bar")
    # print(plt.show())
    plt.savefig("static/images/Sentiment_Count_histogram.png")

    rend = {'positive': positive, 'lenpositive': (len(positive)),
            'negative': negative, 'lennegative': len(negative),
            'neutral': neutral, 'lenneutral': len(neutral),
            'allvalues': len(positive)+len(negative)+len(neutral),
            'positivevalues': Posper, 'negativevalues': Negper, 'neutralvalues': Neugper}
    return render(request, "ProjectHome\VisualPage.html", rend)


def valiemail(emailva):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.fullmatch(regex, emailva)


def Loginuser(request):
    if request.method == "POST":
        login_email = request.POST.get("email")
        passsword = request.POST.get("password")
        print(login_email, passsword)
        try:
            if valiemail(login_email):
                email1 = User.objects.filter(email=login_email)
                user = authenticate(username=email1[0], password=passsword)
            else:
                user = authenticate(username=login_email, password=passsword)
            if user is not None:
                auth_login(request, user)
                messages.success(request, "Successfully Logged In")
                return redirect("/")
            else:
                messages.error(
                    request, "Invalid credentials! Please try again")
                return redirect("/Login")
        except IndexError:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("/Login")
    return render(request, "ProjectHome\Login.html", {})


def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)


def Registeruser(request):
    if request.method == 'POST':
        uname = request.POST.get('usrname')
        email = request.POST.get('Email')
        passwd1 = request.POST.get('Password1')
        passwd2 = request.POST.get('Password2')
        fomtype = "webUser"
        print(uname, email, passwd1, passwd2)
        if len(email) > 200:
            messages.error(
                request, " Your user name must be under 200 characters")
            return redirect('/Register')

        if (passwd1 != passwd2):
            messages.error(request, "Passwords do not match")
            return redirect('/Register')
        username = 'U' + email[:5] + \
            str(random_with_N_digits((len(email) % 5)+1))

        user_email = email
        try:
            existing_user = User.objects.get(email=user_email)
            print("Existing user : ", existing_user)
            if(existing_user.is_active == False):
                print("Active Field false he hai ")
                existing_user.delete()
            else:
                print("1")
                messages.error(request, " Username/Email Already Exists")
                return redirect('/Register')
        except:
            print("here is  starting of error 2")
            myuser = User.objects.create_user(username, email, passwd1)
            myuser.save()
            webUser.objects.create(user=myuser, Susername=username, name=uname,
                                   email=myuser.email, password=myuser.password, usertype=fomtype)
            print("here is error 2")
            print("3")
            messages.error(request, " User created Successfully ! ")
            return redirect('/Login')
    return render(request, "ProjectHome\Register.html", {})


# def Register(request):
#     try:
#         if request.method == "POST":
#             # Get the post parameters
#             username=request.POST.get('username')
#             fname=request.POST.get('Fname')
#             lname=request.POST.get('Lname')
#             email=request.POST.get('email')
#             phonenum = request.POST.get('phonenum')
#             pass1=request.POST.get('password1')
#             pass2=request.POST.get('password2')
#             Address = request.POST.get('Address')
#             city = request.POST.get('city')
#             state = request.POST.get('state')
#             zipcode = request.POST.get('zipcode')
#             usertype = request.POST.get('UserType')

#             # check for errorneous input
#             if len(username) > 10:
#                 messages.error(request, " Your user name must be under 10 characters")
#                 return redirect('/')

#             if not username.isalnum():
#                 messages.error(request, " User name should only contain letters and numbers")
#                 return redirect('/')
#             if (pass1!= pass2):
#                 messages.error(request, " Passwords do not match")
#                 return redirect('/')
#             print(usertype)
#             if usertype == "Buyer":
#                 # Create the user
#                 myuser = User.objects.create_user(username, email, pass1)
#                 myuser.first_name= fname
#                 myuser.last_name= lname
#                 myuser.phonenumber = phonenum
#                 myuser.Address = Address
#                 myuser.city = city
#                 myuser.state = state
#                 myuser.zipcode =  zipcode
#                 myuser.usertype = usertype
#                 myuser.save()
#                 # adding into the group
#                 group = Group.objects.get(name=usertype)
#                 myuser.groups.add(group)
#                 webUser.objects.create(user=myuser,name=fname+lname,email=myuser.email,usertype=myuser.usertype)
#             elif usertype == "Seller":
#                 # Create the user
#                 myuser = User.objects.create_user(username, email, pass1)
#                 myuser.first_name= fname
#                 myuser.last_name= lname
#                 myuser.phonenumber = phonenum
#                 myuser.Address = Address
#                 myuser.city = city
#                 myuser.state = state
#                 myuser.zipcode =  zipcode
#                 myuser.usertype = usertype
#                 myuser.save()
#                 # adding into the group
#                 group = Group.objects.get(name=usertype)
#                 myuser.groups.add(group)
#                 webUser.objects.create(user=myuser,name=fname+" "+lname,email=myuser.email,usertype=myuser.usertype)
#             else:
#                 messages.error(request, " User type selected is invalid ! ")
#             messages.success(request, " Your account has been successfully created")
#             return redirect('/')

#         return render(request,'register.html')
#     except:
#         return HttpResponse("Your Profile May not be Present on server Please Try Again After Some time ! ")

# def Login(request):
#     if request.method=="POST":
#         # Get the post parameters
#         loginusername=request.POST['loginusername']
#         loginpassword=request.POST['loginpassword']

#         user=authenticate(username= loginusername, password= loginpassword)
#         if user is not None:
#             login(request, user)
#             messages.success(request, "Successfully Logged In")
#             return redirect("home")
#         else:
#             messages.error(request, "Invalid credentials! Please try again")
#             return redirect("home")

#     # return HttpResponse("404- Not found")
#     return render(request, 'login.html')


# def Logout(request):
#     logout(request)
#     messages.success(request, "Sucessfully logged out ")
#     return redirect('/')
