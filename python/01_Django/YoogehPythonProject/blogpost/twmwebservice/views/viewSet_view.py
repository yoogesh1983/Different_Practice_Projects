from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from twmblog.models import Post
from twmwebservice.serializer import PostSerializer, UserSerializer
from twmwebservice.authentications import CustomAuthentication


class PostCrudViewUsingViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # Enable DRF authentication and authorization locally
    authentication_classes = [CustomAuthentication, ]
    permission_classes = [IsAuthenticated, ]


class UserCrudViewUsingViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
