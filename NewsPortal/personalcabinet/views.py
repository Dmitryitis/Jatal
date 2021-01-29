from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.
@login_required
def main_personal(request):
    context = {
        'user': request.user
    }
    return render(request, 'personalCabinet.html', context)


@login_required
def cabinet_posts(request):
    return render(request, 'personal-allpost.html')


@login_required
def write_post(request):
    return render(request, 'writepost.html')
