from django.urls import path

from personalcabinet.views import main_personal, cabinet_posts, write_post, single_post, create_comment

urlpatterns = [
    path('cabinet/', main_personal, name='main_personal'),
    path('cabinetposts/', cabinet_posts, name='cabinet_posts'),
    path('writepost/', write_post, name="write_post"),
    path('singlpost/<int:post_id>/', single_post, name='single_post'),
    path('create_comment/<int:post_id>/', create_comment, name='create_comment')
]
