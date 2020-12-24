from django.contrib import admin
from YMSBlog.models import Post,Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'created', 'updated', 'status']

    # The slog will be prepoplated automatically in admin view and will bydefault the 'title' value
    prepopulated_fields = {'slug': ('title',)}

    # This will show the List option for provided columns in a right hand side so that we can filter from these columns
    list_filter = ('status', 'publish', 'updated')

    # This will show the search box and will search from 'title' and 'body' field if we pass anything from there
    search_fields = ('title', 'body')

    #by default it will show all the username in author dropdown list(when adding new post) which is oweful when there are more users.
    # so we don't want to display the author username and just show there input field where we can pass the id(pk) of the user instead
    raw_id_fields = ('author',)

    #First order based on the status. If status is same then order based on the 'publish' column's value
    #Will show the arrow so that we can toggle for assending or descending
    ordering = ['status', 'publish']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'post', 'body', 'created', 'updated', 'active']
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
