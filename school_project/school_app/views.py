from django.contrib import messages, auth
from django.contrib.auth.models import User
from tkinter import messagebox
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
login_required(login_url='login')


def index(request):

    return render(request, 'index.html')


def new(request):
    return render(request, 'new.html')


def store(request):
    if request.method == 'POST':
        messages.success(request, 'Form submitted successfully')
        return redirect('store')

    return render(request, 'store.html')


def register(request):
    if request.method == 'POST':
        user_name = request.POST['Username']
        email = request.POST['e-mail']
        password = request.POST['password']
        cpassword = request.POST['password1']

        if password == cpassword:
            if User.objects.filter(username=user_name).exists():
                messages.error(request, 'Username already exists')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'email already exist')
                return redirect('register')
            else:
                user = User.objects.create_user(username=user_name,
                                                email=email, password=password)
                user.save()
                print("user created")
                return redirect('login')
        else:
            messages.error(request, "Password not matching")
            return redirect('register')

    return render(request, 'register.html')


def login_page(request):
    if request.method == 'POST':
        user_name = request.POST.get('Username')
        password = request.POST.get('password')
        user = auth.authenticate(username=user_name, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('new')
        else:
            messages.error(request, 'invalid credentials')
            return redirect('login')

    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
