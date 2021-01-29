from django.shortcuts import render


# Create your views here.
def all_posts(request):
    return render(request, 'allpost.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')
