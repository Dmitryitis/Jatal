from django.urls import path

from personalcabinet.views import main_personal, cabinet_posts, write_post, single_post

urlpatterns = [
    path('cabinet/', main_personal, name='main_personal'),
    path('cabinetposts/', cabinet_posts, name='cabinet_posts'),
    path('writepost/', write_post, name="write_post"),
    path('singlpost/<int:post_id>/', single_post, name='single_post')
]
