from django.shortcuts import render


# Create your views here.
def main_page(request):
    return render(request, 'index.html')


def all_posts(request):
    return render(request, 'allpost.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')
