from django import forms

from personalcabinet.models import Post


class CreatePost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'photo', 'text',)
