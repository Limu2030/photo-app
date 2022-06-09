from django.contrib import admin

# Register your models here.

from .models import Profile, Post, Following, Follower, Comment

admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Following)
admin.site.register(Follower)
admin.site.register(Comment)