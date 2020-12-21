from django.contrib import admin
from YMSBlog.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'created', 'updated', 'status']

admin.site.register(Post, PostAdmin)
