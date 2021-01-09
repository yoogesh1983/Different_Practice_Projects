from rest_framework.viewsets import ModelViewSet
from twmblog.models import Post
from twmwebservice.serializer import PostSerializer


class PostCrudViewUsingViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer