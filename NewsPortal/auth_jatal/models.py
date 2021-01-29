from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.TextField(null=True, verbose_name='about')

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
