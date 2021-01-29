from django.contrib import admin

# Register your models here.
from auth_jatal.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('about',)


admin.site.register(Profile, ProfileAdmin)
