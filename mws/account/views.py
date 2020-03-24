from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import login, authenticate
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
import json
from .forms import UserForm
# Create your views here.
def post_index(request):
    if request.method =='POST':
        username= request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username= username, password= password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'username or passowrd is not correct'})
    return render(request, 'login.html')

def post_sign_up(request):
    if request.method =='POST':
        user = User.objects.create_user(username=request.POST['username'], password= request.POST['password'])
        auth.login(request, user)
        return redirect('home')
    return render(request, 'signup.html')
def index(request):
    if request.method =="POST":
        if request.POST['password1'] == request.POST["password2"]:
            user = User.objects.create_user(
                username=request.POST["username"],password=request.POST["password1"]
            )
            auth.login(request,user)
            return render(request, 'index.html')
        return render(request, 'login')

    return render(request, 'index.html')

def login1(request):
    if request.method =="POST":
        username = request.POST["username"]
        password1 = request.POST['password1']
        user = auth.authenticate(request, username = username, password=password1)
        if user is not None:
            auth.login(request, user)
            return redirect('http://127.0.0.1:8000/blog/day/')
        else:
            return render(request, "index2.html",{'error':'username or password is incorrect'})
    else:
        return render(request, 'index2.html')
def logout(request):
    auth.logout(request)
    return redirect('http://127.0.0.1:8000/blog/day/')
def comp(request):
    context=[

    ]
    return render(request, 'comp.html',context=context)