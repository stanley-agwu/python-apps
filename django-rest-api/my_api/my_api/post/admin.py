from django.contrib import admin
from .models import Post, PostsRate

# Register your models here.
admin.site.register(Post)
admin.site.register(PostsRate)