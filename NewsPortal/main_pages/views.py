from django.shortcuts import render


# Create your views here.
def main_page(request):
    if request.user.is_authenticated:
        print(request.user)
        context = {
            'user': request.user,
        }
        return render(request, 'index.html', context)
    return render(request, 'index.html', {'user': ''})


def all_posts(request):
    return render(request, 'allpost.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')
