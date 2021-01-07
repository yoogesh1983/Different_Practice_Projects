from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveDestroyAPIView, \
    RetrieveUpdateAPIView, ListCreateAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from twmblog.models import Post
from twmwebservice.serializer import PostSerializer


########################################################################################
# Using Django framework API-View
########################################################################################

class PostListAPIView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        queryset = Post.objects.all()
        pk = self.request.GET.get('id')  # when you pass /?id=4
        if pk is not None:
            queryset = queryset.filter(id__iexact=pk)
        serializer = PostSerializer(queryset, many=True)
        dict_data = serializer.data
        # The Response method internally convert the Python_dictionary data into Json and return the Json response to the end user
        return Response(dict_data)


class PostListAPIView_ShortCutWay(ListAPIView):
    # queryset = Post.objects.all()    # queryset is defined and cannot be other that it. require here if we don't override get_queryset() method
    serializer_class = PostSerializer  # serializer_class is defined and cannot be other

    # If you want the customized list as a response then you need to override this.
    # It is used especially to implement search operation
    def get_queryset(self):
        queryset = Post.objects.all()
        pk = self.request.GET.get('id')  # when you pass /?id=4
        if pk is not None:
            queryset = queryset.filter(id__iexact=pk)
        return queryset


class PostCreateAPIView_ShortCutWay(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostRetrieveAPIView_ShortCutWay(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'id'  # default lookup field is 'pk'


class PostUpdateAPIView_ShortCutWay(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'id'  # default lookup field is 'pk'


class PostDestroyAPIView_ShortCutWay(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'id'  # default lookup field is 'pk'

#####################################################################
############################### List and Create both at the same class ####
class PostListAndCreateAPIView_ShortCutWay(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    def get_queryset(self):
        queryset = Post.objects.all()
        pk = self.request.GET.get('id')  # when you pass /?id=4
        if pk is not None:
            queryset = queryset.filter(id__iexact=pk)
        return queryset

class PostRetrieveAndUpdateAPIView_ShortCutWay(RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'id'  # default lookup field is 'pk'

class PostRetrieveAndDestroyAPIView_ShortCutWay(RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'id'  # default lookup field is 'pk'

class PostRetrieveUpdateAndDestroyAPIView_ShortCutWay(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'id'  # default lookup field is 'pk'