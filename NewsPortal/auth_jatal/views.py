from django.shortcuts import render


# Create your views here.
def main_login(request):
    return render(request, 'login.html')


def auth(request):
    return render(request, 'login2.html')


def registration(request):
    return render(request, 'registration.html')
