from django.urls import path

from personalcabinet.views import main_personal

urlpatterns = [
    path('cabinet/', main_personal, name='main_personal'),
]
