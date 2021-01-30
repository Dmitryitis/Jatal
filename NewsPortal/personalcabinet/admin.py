from django.contrib import admin

# Register your models here.
from personalcabinet.models import Topic, Post


class TopicAdmin(admin.ModelAdmin):
    list_display = ('name',)


class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'date_create')


admin.site.register(Topic, TopicAdmin)
admin.site.register(Post, PostAdmin)
