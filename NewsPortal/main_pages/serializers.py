from rest_framework.serializers import ModelSerializer

from personalcabinet.models import Post


class PostsSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['pk', 'title', 'photo', 'text', 'author', 'date_create', 'topic']
