from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from auth_jatal.forms import AuthForm, RegistrationForm


def main_login(request):
    return render(request, 'login.html')


def auth_jatal(request):
    if request.method == 'POST':
        form = AuthForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('main_page')
            else:
                context = {
                    'error_auth': 'Неправильный логин или пароль'
                }
                return render(request, 'login2.html', context)

    return render(request, 'login2.html', {'error_auth': ''})


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            rep_password = form.cleaned_data['rep_password']
            firstname = form.cleaned_data['first_name']
            lastname = form.cleaned_data['last_name']

            if password == rep_password:
                User.objects.create(username=username, email=email, password=make_password(password),
                                    first_name=firstname, last_name=lastname)
                return redirect('main_login')
    return render(request, 'registration.html')


def logout_view(request):
    logout(request)
    return redirect('main_page')


def main_page(request):
    if request.user.is_authenticated:
        print(request.user)
        context = {
            'user': request.user,
        }
        print('dfsdf')
        return render(request, 'index.html', context)
    return render(request, 'index.html', {'user': ''})
