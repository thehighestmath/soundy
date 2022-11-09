from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin

from .models import Blogger, Musician, CustomUser


class BloggerAdmin(ModelAdmin):
    model = Blogger


class MusicianAdmin(ModelAdmin):
    model = Musician


class CustomUserAdmin(UserAdmin):
    list_display = (
        'username', 'email', 'first_name', 'last_name', 'is_staff',
        'is_blogger', 'is_musician'
    )


admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(Musician, MusicianAdmin)
admin.site.register(Blogger, BloggerAdmin)
