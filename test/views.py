from multiprocessing import context
from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import LoginForm
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request,'index.html')

def login_page(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        print(form)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            print(username)
            password = form.cleaned_data.get('password')
            print(password)
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("index")
            else:
                return redirect('https://www.youtube.com/watch?v=RyK-A_dGbBw')
        else:
            messages.error(request,"bulaşma ulan")
    return render(request,'login.html',context={'form':form})

def logout_user(request):
    logout(request)
    return redirect('login')

@login_required(login_url='/pentestivirzivir/login')
def pentestivirzivirView(request):
    return render(request,'pentestivirzivir.html')
# Create your views here.
