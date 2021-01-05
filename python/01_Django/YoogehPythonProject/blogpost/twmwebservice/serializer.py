import string

from rest_framework import serializers
from twmblog.models import Post


class PostSerializer(serializers.ModelSerializer):

    def title_should_not_be_state_farm(value):
        print('This is called..........')
        if value == 'statefarm':
            raise serializers.ValidationError('Title Should not be state-farm')
        return value

    title = serializers.CharField(validators=[title_should_not_be_state_farm])

    class Meta:
        model = Post
        fields = '__all__'
