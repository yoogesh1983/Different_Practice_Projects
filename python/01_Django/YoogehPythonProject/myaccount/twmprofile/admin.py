from django.contrib import admin
from twmprofile.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'created', 'updated', 'status']

admin.site.register(Post, PostAdmin)
