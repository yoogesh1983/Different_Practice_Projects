from rest_framework import generics, mixins
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveDestroyAPIView, \
    RetrieveUpdateAPIView, ListCreateAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from twmblog.models import Post
from twmwebservice.serializer import PostSerializer


class PostListViewMixin(generics.ListAPIView):
    # queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        queryset = Post.objects.all()
        pk = self.request.GET.get('id')  # when you pass /?id=4
        if pk is not None:
            queryset = queryset.filter(id__iexact=pk)
        return queryset


class PostListAndCreateViewMixin(mixins.CreateModelMixin, generics.ListAPIView):
    #queryset = Post.objects.all()
    serializer_class = PostSerializer
    #@Override
    def get_queryset(self):
        queryset = Post.objects.all()
        pk = self.request.GET.get('id')  # when you pass /?id=4
        if pk is not None:
            queryset = queryset.filter(id__iexact=pk)
        return queryset
    #@Override
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PostRetrieveUpdateAndDestroyModelMixin(generics.RetrieveAPIView, mixins.DestroyModelMixin, mixins.UpdateModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    #@Override
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    #@Override
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    #@Override
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
