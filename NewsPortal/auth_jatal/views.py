from django.contrib.auth import logout
from django.shortcuts import render, redirect


def main_login(request):
    return render(request, 'login.html')


def auth(request):
    return render(request, 'login2.html')


def registration(request):
    return render(request, 'registration.html')


def logout_view(request):
    logout(request)
    return redirect('main_page')
