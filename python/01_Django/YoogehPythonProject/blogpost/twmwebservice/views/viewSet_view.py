from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from twmblog.models import Post
from twmwebservice.serializer import PostSerializer


class PostCrudViewUsingViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def list(self, request):
        queryset = Post.objects.all()
        pk = self.request.GET.get('id')  # when you pass /?id=4
        if pk is not None:
            queryset = queryset.filter(id__iexact=pk)
        serializer = PostSerializer(queryset, many=True)
        dict_data = serializer.data
        # The Response method internally convert the Python_dictionary data into Json and return the Json response to the end user
        return Response(dict_data)