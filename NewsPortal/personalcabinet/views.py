from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core import  serializers
# Create your views here.
from personalcabinet.forms import CreatePost
from personalcabinet.models import Topic, Post


@login_required
def main_personal(request):
    context = {
        'user': request.user
    }
    return render(request, 'personalCabinet.html', context)


@login_required
def cabinet_posts(request):
    posts = Post.objects.filter(author=request.user)
    context = {
        'posts': posts
    }
    return render(request, 'personal-allpost.html', context)


@login_required
def write_post(request):
    if request.method == 'POST':
        form = CreatePost(request.POST, request.FILES)

        if form.is_valid():
            title = form.cleaned_data['title']
            photo = form.cleaned_data['photo']
            text = form.cleaned_data['text']
            author = request.user
            topic = Topic.objects.get(name=request.POST['topic'])

            Post.objects.create(title=title, photo=photo, text=text, author=author, topic=topic)
            return redirect('cabinet_posts')

    topics = Topic.objects.all()
    context = {
        'topics': topics
    }
    return render(request, 'writepost.html', context)


def single_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    context = {
        'post': post,
    }
    return render(request, 'singlepost.html', context)
