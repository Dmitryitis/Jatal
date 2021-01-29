from django.urls import path

from auth_jatal.views import main_login, auth, registration, logout_view

urlpatterns = [
    path('main_auth/', main_login, name='main_login'),
    path('auth/', auth, name='auth_jatal'),
    path('registration/', registration, name='registration'),
    path('logout/', logout_view, name='logout'),
]
