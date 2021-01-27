from django.urls import path

from auth_jatal.views import main_login, auth, registration

urlpatterns = [
    path('', main_login, name='main_login'),
    path('auth/', auth, name='auth_jatal'),
    path('registration/', registration, name='registration')
]
