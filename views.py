from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
model = LogisticRegression(max_iter=1000)
from sklearn.metrics import accuracy_score
from django.contrib import messages
from django.http import HttpResponse
def home_page(request):
    return render(request,'header.html')
def login_signup(request):
    return render(request, 'login_signup.html')
def signup(request):
    if request.method=='POST':
        uname=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['conpassword']
        if User.objects.filter(username=uname).exists() or User.objects.filter(email=email).exists():
            messages.error(request,'username or email is already Exist')
            return redirect('signup')
        elif password!=confirm_password:
            messages.error(request,'Password and Confirm Password')
            return redirect('signup')
        else:
            newuser=User(username=uname,email=email)
            newuser.set_password(password)
            newuser.save()
            return redirect('login')

    return render(request, 'signup.html')

def user_login(request):
    if request.method=='POST':
        uname=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=uname,password=password)
        if user is not None:
            login(request,user)
            redirect('/')
    return render(request, 'login.html')
def logout_view(request):
    logout(request)
    # Redirect to a desired page after logout, e.g., home page
    return redirect('login')

# def login(request):
#     if request.method=='POST':
#         uname=request.POST['username']
#         password=request.POST['password']
#         user=authenticate(request,username=uname,password=password)
#         if user is not None:
#             login(request,user)
#             redirect('predict')
#     return render(request,'loginwithsignup.html') #DiabetesPrediction/templates/loginwithsignup.html
# def sign_up_view(request):
#     if request.method=='POST':
#         uname=request.POST['username2']
#         email=request.POST['email2']
#         password=request.POST['password3']
#         confirm_password=request.POST['password4']
#         if User.objects.filter(username=uname).exists() or User.objects.filter(email=email).exists():
#             messages.error(request,'username or email is already Exist')
#             return redirect('login')
#         elif password!=confirm_password:
#             messages.error(request,'Password and Confirm Password')
#             return redirect('login')
#         else:
#             newuser=User(username=uname,email=email)
#             newuser.set_password(password) 
#             newuser.save()
#             return redirect('login')
#     return render(request,'loginwithsignup.html')
def home(request):
    return render(request, 'home.html')
def predict(request):
    return render(request, 'predict.html')
def result(request):
    data = pd.read_csv(r"C:\Users\ASUS\Downloads\SWE Project\diabetes.csv")

    X = data.drop("Outcome", axis=1)
    Y = data['Outcome']
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
    X_train

    model = LogisticRegression()
    model.fit(X_train, Y_train)

    val1 = float(request.GET['n1'])
    val2 = float(request.GET['n2'])
    val3 = float(request.GET['n3'])
    val4 = float(request.GET['n4'])
    val5 = float(request.GET['n5'])
    val6 = float(request.GET['n6'])
    val7 = float(request.GET['n7'])
    val8 = float(request.GET['n8'])

    pred = model.predict([[val1, val2, val3, val4, val5, val6, val7, val8]])

    result2 = ""
    if pred==[1]:
        result1 = "Oops! You have DIABETES ????."
    else:
        result1 = "Great! You DON'T have Diabetes ????."

    return render(request, "predict.html", {"result2":result1})
