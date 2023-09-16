from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def home(request):

    #check if user is logging in
    if request.method == 'POST':
        print(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.info(request, 'Logged in successfully')
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect')
            return redirect('home')
    return render(request, 'home.html', {})

def logout_user(request):
    logout(request)
    messages.info(request, 'Logged out successfully')
    return redirect('home')

# User registration
def register_user(request):
    if request.method == 'POST':
        print(request.POST)
    return render(request, 'register.html', {})




