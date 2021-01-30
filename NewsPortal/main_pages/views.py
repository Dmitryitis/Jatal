from django.shortcuts import render
from django.core import serializers

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from main_pages.serializers import PostsSerializer
from personalcabinet.models import Post, Topic


class PostsView(ModelViewSet):
    queryset = Post.objects.all().order_by('-date_create')
    serializer_class = PostsSerializer


def all_posts(request):
    topics = Topic.objects.all()
    if request.method == 'POST':
        topic = Topic.objects.filter(name=request.POST['val'])
        search = request.POST['search']
        if topic:
            posts = Post.objects.filter(topic=topic[0])
            context = {
                'posts': posts,
                'topics': topics
            }
            shortener_text(posts)
            return render(request, 'allpost.html', context)
    posts = Post.objects.all().order_by('-date_create')
    shortener_text(posts)
    context = {
        'posts': posts,
        'topics': topics
    }
    return render(request, 'allpost.html', context)


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def shortener_text(posts):
    for post in posts:
        words = post.text.split(" ")
        if len(words) > 60:
            post.text = ''
            for word in range(60):
                post.text += words[word] + ' '
        post.text += '....'
