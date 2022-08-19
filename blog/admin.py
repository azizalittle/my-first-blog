from django.contrib import admin
# imports the Post created in blog/models.py
from .models import Post

# Register your models here.

admin.site.register(Post)