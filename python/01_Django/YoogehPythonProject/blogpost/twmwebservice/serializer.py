import string

from django import forms
from rest_framework import serializers
from taggit.models import Tag
from twmblog.models import Post
from django.contrib.auth.models import User
from django.utils import timezone

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('url', 'id', 'name')

class PostSerializer(serializers.ModelSerializer):

    def title_should_not_be_state_farm(value):
        if value is not None and type(value) == string and value.lower() == 'State-Farm':
            raise serializers.ValidationError('Title Should not be State-Farm')
        return value

    title = serializers.CharField(validators=[title_should_not_be_state_farm])

    class Meta:
        model = Post
        fields = ('title', 'body', 'tags', 'status')
