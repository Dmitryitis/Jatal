from django.urls import path

from personalcabinet.views import main_personal, cabinet_posts, write_post

urlpatterns = [
    path('cabinet/', main_personal, name='main_personal'),
    path('cabinetposts/', cabinet_posts, name='cabinet_posts'),
    path('writepost/', write_post, name="write_post")
]
