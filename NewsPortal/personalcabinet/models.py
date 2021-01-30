import PIL
from django.contrib.auth.models import User
from django.db import models
from PIL import Image


# Create your models here.
class Topic(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='title')
    photo = models.ImageField(upload_to='images/', verbose_name='photo')
    text = models.TextField(verbose_name='text')
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_create = models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def save(self, **kwargs):
        super().save()

        img = Image.open(self.photo.path)
        img.resize((1920, 1280), PIL.Image.ANTIALIAS)
        img.save(self.photo.path, format='JPEG', quality=85, progressive=True)
