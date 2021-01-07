import datetime
import io

from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from twmblog.models import Post
from twmwebservice.mixin import HttpResponseMixin
from twmwebservice.serializer import PostSerializer


########################################################################################
# Using Django framework API-View [Core]
########################################################################################

class PostListAPIViewFor_Get_GetAll_and_Post(APIView, HttpResponseMixin):

    #@Override
    def get(self, request, format=None, *args, **kwargs):
        queryset = Post.objects.all()
        pk = self.request.GET.get('id')  # when you pass /?id=4
        if pk is not None:
            queryset = queryset.filter(id__iexact=pk)
        serializer = PostSerializer(queryset, many=True)
        dict_data = serializer.data
        # The Response method internally convert the Python_dictionary data into Json and return the Json response to the end user
        return Response(dict_data)

    #@Override
    def post(self, request, format=None, *args, **kwargs):
        byte = request.body
        stream = io.BytesIO(byte)
        dict_data = JSONParser().parse(stream)
        self.generateRequireFields(dict_data)
        serializer = PostSerializer(data=dict_data)
        if serializer.is_valid():
            try:
                serializer.save()
            except Exception as msg:
                msg = {'msg': '{}'.format(msg)}
            else:
                msg={'msg': 'Successfully saved the Data into database'}
        else:
            msg = {'msg': '{}'.format(serializer.errors)}
        return Response(msg)


class PostListAPIViewFor_Get_Put_Patch_and_Delete(APIView):

    #@Override
    def put(self, request, id, format=None, *args, **kwargs):
        try:
            post = Post.objects.get(id=id)
        except Post.DoesNotExist:
            msg={'msg': 'Post object with id {} does not exist.'.format(id)}
        else:
            byte = request.body
            stream = io.BytesIO(byte)
            dict_data = JSONParser().parse(stream)
            serializer = PostSerializer(post, data=dict_data)
            if serializer.is_valid():
                try:
                    serializer.save()
                except Exception as msg:
                    msg = {'msg': '{}'.format(msg)}
                else:
                    msg={'msg': 'Post object with id {} have Fully been updated.'.format(id)}
            else:
                msg = {'msg': '{}'.format(serializer.errors)}
        return Response(msg)

    #@Override
    def patch(self, request, id, format=None, *args, **kwargs):
        try:
            post = Post.objects.get(id=id)
        except Post.DoesNotExist:
            msg={'msg': 'Post object with id {} does not exist.'.format(id)}
        else:
            byte = request.body
            stream = io.BytesIO(byte)
            dict_data = JSONParser().parse(stream)
            dict_data['publish'] = datetime.datetime.now()
            serializer = PostSerializer(post, data=dict_data, partial=True)
            if serializer.is_valid():
                try:
                    serializer.save()
                except Exception as msg:
                    msg = {'msg': '{}'.format(msg)}
                else:
                    msg={'msg': 'Post object with id {} have partially been updated.'.format(id)}
            else:
                msg = {'msg': '{}'.format(serializer.errors)}
        return Response(msg)

    #@Override
    def delete(self, request, id, format=None, *args, **kwargs):
        try:
            post = Post.objects.get(id=id)
        except Post.DoesNotExist:
            msg={'msg': 'Post object with id {} does not exist.'.format(id)}
        else:
            status, deleted_item = post.delete()
            if status == 1:
                msg = {'msg': 'Post with id {} has successfully been deleted'.format(id)}
            else:
                msg = {'msg': 'Error occured while trying to delete Post with id {}. Try again later'.format(id)}
        return Response(msg)