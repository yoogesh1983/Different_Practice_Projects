import string

from rest_framework import serializers
from twmblog.models import Post


class PostSerializer(serializers.ModelSerializer):

    def title_should_not_be_state_farm(value):
        if value == 'yms':
            raise serializers.ValidationError('Title Should not be yms')
        return value

    title = serializers.CharField(validators=[title_should_not_be_state_farm])

    class Meta:
        model = Post
        fields = '__all__'
