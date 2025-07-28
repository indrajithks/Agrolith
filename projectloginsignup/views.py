from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Vegetable


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
            return render(request, 'welcome.html', {'login_error': 'Invalid credentials'})
        
    return render(request, 'login.html')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username').strip()
        email = request.POST.get('email')
        password = request.POST.get('password1')

        if User.objects.filter(username=username).exists():
            return render(request, 'welcome.html', {'signup_error': 'Username already exists.'})
        
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        login(request, user)

        return redirect('dashboard')

    return redirect('home')

def dashboard_view(request):
    return render(request, 'dashboard.html')

def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home')

def dashboard_view(request):
    vegetables = Vegetable.objects.all()
    return render(request, 'dashboard.html', {'vegetables': vegetables})
