import json

from django.contrib.auth.models import User
from django.core.serializers import serialize
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import View
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from twmblog.forms import AddPostRequest
from twmblog.models import Post
from twmwebservice.serializer import PostSerializer
from twmwebservice import twmUtil
from twmwebservice.mixin import HttpResponseMixin


##################################################################################
# By using Function Based View
##################################################################################
def get_post_by_using_function_based_view(request):
    # This is dictionary
    dict_data = {'title': 'This is title', 'body': 'This is body', }

    # we need to convert dictionary into Json by using dumps() method
    # json_data = json.dumps(dict_data)
    # return HttpResponse(json_data, content_type='application/json')

    # Or you can use this method which does above tasks by this single line
    return JsonResponse(dict_data)


########################################################################################
# Without using Django provided Rest Framework [Our own framework i.e. Durga Framework]
########################################################################################
@method_decorator(csrf_exempt, name='dispatch')
class PostDetailCBV(HttpResponseMixin, View):
    # @Override
    def get(self, request, id, *args, **kwargs):
        try:
            post = Post.objects.get(id=id)
        except Post.DoesNotExist:
            json_data = json.dumps({'msg': 'The requested resource is not available'})
            return self.render_to_http_response(json_data, 400)
        else:
            json_data = self.remove_meta_data(
                serialize('json', [post, ]))  # Serialize() method required list as argument
            return self.render_to_http_response(json_data)

    # @Override
    def put(self, request, id, *args, **kwargs):
        try:
            post = Post.objects.get(id=id)
        except Post.DoesNotExist:
            json_data = json.dumps({'msg': 'The requested id could not be found!!'})
            return self.render_to_http_response(json_data, 404)
        else:
            json_data = request.body
            valid_json = twmUtil.is_valid_json(json_data)
            if not valid_json:
                json_data = json.dumps({'msg': 'Invalid Json Format!'})
                return self.render_to_http_response(json_data, 400)
            dict_data = json.loads(json_data)
            dict_post_data = json.loads(serialize('json', [post, ]))[0]
            dict_post_data.update(dict_data)
            print(dict_post_data)

            form = AddPostRequest(dict_post_data, instance=post)
            if form.is_valid():
                try:
                    post = form.save(commit=True)
                except Exception as msg:
                    json_data = json.dumps({'msg': '{}'.format(msg)})
                    return self.render_to_http_response(json_data, 500)
                else:
                    json_data = json.dumps({'msg': 'Successfully updated the data!'})
                    return self.render_to_http_response(json_data)
            if form.errors:
                json_data = json.dumps(form.errors)
                return self.render_to_http_response(json_data, 400)

    # @Override
    def delete(self, request, id, *args, **kwargs):
        try:
            post = Post.objects.get(id=id)
        except Post.DoesNotExist:
            json_data = json.dumps({'msg': 'The requested id could not be found. Could not delete the item!!'})
            return self.render_to_http_response(json_data, 404)
        else:
            status, deleted_item = post.delete()
            if status == 1:
                json_data = json.dumps({'msg': 'Successfully deleted the data! {}'.format(deleted_item)})
                return self.render_to_http_response(json_data, 500)
            else:
                json_data = json.dumps({'msg': 'Unable to delete. please try again!'})
                return self.render_to_http_response(json_data)


@method_decorator(csrf_exempt, name='dispatch')
class PostListCBV(HttpResponseMixin, View):
    # @Override
    def get(self, request, *args, **kwargs):
        try:
            posts = Post.objects.all()
        except Post.DoesNotExist:
            json_data = json.dumps({'msg': 'The requested resource is not available'})
            return self.render_to_http_response(json_data, 400)
        else:
            json_data = self.remove_meta_data(serialize('json', posts, fields=('title', 'slug')))
            return self.render_to_http_response(json_data)

    # @Override
    def post(self, request, *args, **kwargs):
        json_data = request.body
        valid_json = twmUtil.is_valid_json(json_data)
        if not valid_json:
            json_data = json.dumps({'msg': 'Invalid Json Format!'})
            return self.render_to_http_response(json_data, 400)

        dict_data = json.loads(json_data)
        form = AddPostRequest(dict_data)
        if form.is_valid():
            try:
                post = form.save(commit=False)
                post.author = User.objects.get(username='dba@gmail.com')
                post.slug = post.title.replace(" ", "").lower()
                post.save()
            except Exception as msg:
                json_data = json.dumps({'msg': '{}'.format(msg)})
                return self.render_to_http_response(json_data, 500)
            else:
                json_data = json.dumps({'msg': 'Successfully saved the data!'})
                return self.render_to_http_response(json_data)
        if form.errors:
            json_data = json.dumps(form.errors)
            return self.render_to_http_response(json_data, 400)

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
        #The Response method internally convert the Python_dictionary data into Json and return the Json response to the end user
        return Response(dict_data)

class PostListAPIView_ShortCutWay(ListAPIView):
    #queryset = Post.objects.all()    # queryset is defined and cannot be other that it. require here if we don't override get_queryset() method
    serializer_class = PostSerializer # serializer_class is defined and cannot be other

    #If you want the customized list as a response then you need to override this.
    #It is used especially to implement search operation
    def get_queryset(self):
        queryset = Post.objects.all()
        pk = self.request.GET.get('id')
        if pk is not None:
            queryset = queryset.filter(id__iexact=pk)
        return queryset

class PostCreateAPIView_ShortCutWay(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer








