from django.urls import path

from main_pages.views import main_page, all_posts, about, contact

urlpatterns = [
    path('', main_page, name='main_page'),
    path('posts/', all_posts, name='all_posts'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
]
