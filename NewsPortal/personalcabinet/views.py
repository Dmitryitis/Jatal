from django.shortcuts import render


# Create your views here.
def main_personal(request):
    return render(request, 'personalCabinet.html', )
