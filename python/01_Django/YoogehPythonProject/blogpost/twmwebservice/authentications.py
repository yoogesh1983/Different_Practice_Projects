from django.contrib.auth.models import User
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed


class CustomAuthentication(BaseAuthentication):
    def authenticate(self, request):
        username = request.GET.get('username')
        if username is None:
            return None  # The response you will get because of this is 'The authentication credentials are not provided'
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            raise AuthenticationFailed('Username you provided did not match in our database')
        return User, None
