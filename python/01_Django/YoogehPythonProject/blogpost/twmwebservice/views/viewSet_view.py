from rest_framework.viewsets import ModelViewSet
from rest_framework import generics, mixins
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveDestroyAPIView, \
    RetrieveUpdateAPIView, ListCreateAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from twmblog.models import Post
from twmwebservice.serializer import PostSerializer


class PostCrudViewUsingViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

