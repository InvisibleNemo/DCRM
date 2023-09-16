from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, RecordForm
from .models import Record



# Create your views here.

def home(request):

    records = Record.objects.all()



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
    return render(request, 'home.html', {'records': records})




def logout_user(request):
    logout(request)
    messages.info(request, 'Logged out successfully')
    return redirect('home')

# User registration
def register_user(request):
    if request.method == 'POST':
        
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Registration successful')
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})

    return render(request, 'register.html', {'form': form})


def customer_record(request, pk):

    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        
        return render(request, 'customer_record.html', {'customer_record': customer_record})
    else:
        messages.info(request, 'You are not logged in')
        return redirect('home')
    

def customer_record_delete(request, pk):

    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        customer_record.delete()
        messages.success(request, 'Record deleted successfully')
        return redirect('home')
    else:
        messages.info(request, 'You are not logged in')
        return redirect('home')

def customer_record_new(request):

    if request.user.is_authenticated:
        if request.method == 'POST':
            form = RecordForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Record added successfully')
                return redirect('home')
        else:
            form = RecordForm()
            return render(request, 'customer_record_new.html', {'form': form})
    else:
        messages.info(request, 'You are not logged in')
        return redirect('home')
    
def customer_record_update(request, pk):

    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        if request.method == 'POST':
            form = RecordForm(request.POST, instance=customer_record)
            if form.is_valid():
                form.save()
                messages.success(request, 'Record updated successfully')
                return redirect('home')
        else:
            form = RecordForm(instance=customer_record)
            return render(request, 'customer_record_update.html', {'form': form})
    else:
        messages.info(request, 'You are not logged in')
        return redirect('home')    