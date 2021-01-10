from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly
from rest_framework.viewsets import ModelViewSet
from twmblog.models import Post
from twmwebservice.serializer import PostSerializer
from twmwebservice.permissions import IsCustomSatisfied


class PostCrudViewUsingViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # Enable DRF authentication and authorization locally
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsCustomSatisfied,]