from django.contrib import admin
from django.contrib.admin.decorators import register
from blog.models import Comment, Post , newauth
# Register your models here.
admin.site.register(Comment)
admin.site.register(Post)
admin.site.register(newauth)
