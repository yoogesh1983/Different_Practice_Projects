from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveDestroyAPIView, \
    RetrieveUpdateAPIView, ListCreateAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework.pagination import PageNumberPagination
from twmblog.models import Post
from twmwebservice.serializer import PostSerializer


class MyPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'page'  # which page you want to display i.e. /?page = 3  [default value is 'page']
    page_size_query_param = 'qty'  # How many objects you would want to display on per page? i.e. /?page=3&qty=2
    max_page_size = 15  # You can't ask more than 15 size
    last_page_strings = ('lastpage',)  # get the last page  i.e. /?page=lastpage  [default value is ('last',)


########################################################################################
# Using Django framework API-View
########################################################################################
class PostListAPIView_ShortCutWay(ListAPIView):
    # queryset = Post.objects.all()    # queryset is defined and cannot be other that it. require here if we don't override get_queryset() method
    serializer_class = PostSerializer  # serializer_class is defined and cannot be other
    pagination_class = MyPagination

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
