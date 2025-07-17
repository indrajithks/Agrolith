from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def welcome_view(request):
    return render(request,'welcome.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username').strip()
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return HttpResponse("Invalid credientials")
        
    return render(request, 'login.html')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username').strip()
        email = request.POST.get('email')
        password = request.POST.get('password1')

        if User.objects.filter(username=username).exists():
            return HttpResponse("Username already exists!")
        
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        print("created user:", user.username)
        print("Password hash", user.password)

        return redirect('login')

    return render(request, 'signup.html')

def dashboard_view(request):
    return render(request, 'dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('login')