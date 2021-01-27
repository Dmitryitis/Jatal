from django.shortcuts import render


# Create your views here.
def main_personal(request):
    return render(request, 'personalCabinet.html', )


def cabinet_posts(request):
    return render(request, 'personal-allpost.html')


def write_post(request):
    return render(request, 'writepost.html')
