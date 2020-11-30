from django.contrib import admin
from twmprofile.models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'firstName', 'age']

admin.site.register(Profile, ProfileAdmin)
