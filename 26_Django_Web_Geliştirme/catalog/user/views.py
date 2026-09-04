from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

# Create your views here.

def login(request):
    if request.method == 'POST':  # butona tıklandı mı?
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username= username, password= password)  # Varsa user'ı döndürür.
        if user is not None:
            auth.login(request, user)  # session id oluşturur
            messages.add_message(request, messages.SUCCESS, "Logged in successfully.")
            return redirect('index')
        else:
            messages.add_message(request, messages.ERROR, "Couldn't logged in!")
            return redirect('login')
    else:
        return render(request, 'user/login.html')

def register(request):
    if request.method == 'POST':

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repassword = request.POST['repassword']

        if password == repassword:
            if User.objects.filter(username = username).exists():
                messages.add_message(request, messages.WARNING, "Username is already taken.")
                return redirect('register')
            else:
                if User.objects.filter(email = email).exists():
                    messages.add_message(request, messages.WARNING, "Email is already taken.")
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, password=password, email=email)
                    user.save()
                    messages.add_message(request, messages.SUCCESS, "User created successfully.")
                    return redirect('login')
        else:
            messages.add_message(request, messages.WARNING, "Passwords do not match.")
        return redirect('register')
    else:
        return render(request, 'user/register.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.add_message(request, messages.SUCCESS, 'Logged out successfully.')
        return redirect('index')