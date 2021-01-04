import json

from django.contrib.auth.models import User
from django.core.serializers import serialize
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import View
from rest_framework.renderers import JSONRenderer
from twmblog.forms import AddPostRequest
from twmblog.models import Post
from twmwebservice import twmUtil
from twmwebservice.mixin import HttpResponseMixin
from twmwebservice.serializer import PostSerializer


##################################################################################
#By using Function Based View
##################################################################################
def get_post_by_using_function_based_view(request):
    # This is dictionary
    dict_data = {'title': 'This is title', 'body' : 'This is body',}

    #we need to convert dictionary into Json by using dumps() method
    #json_data = json.dumps(dict_data)
    #return HttpResponse(json_data, content_type='application/json')

    #Or you can use this method which does above tasks by this single line
    return JsonResponse(dict_data)



########################################################################################
#Without using Django provided Rest Framework [Our own framework i.e. Durga Framework]
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
#Using Django RestFramework
########################################################################################
@method_decorator(csrf_exempt, name='dispatch')
class PostDetailDRF(HttpResponseMixin, View):
    # @Override
    def get(self, request, id, *args, **kwargs):
        try:
            post = Post.objects.get(id=id)
            eserializer = PostSerializer(post)
        except Post.DoesNotExist:
            json_data = json.dumps({'msg': 'The requested resource is not available'})
            return self.render_to_http_response(json_data, 400)
        else:
            print("=====")
            json_data = json.dumps(eserializer.data)
            print(json_data)
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
class PostListDRF(HttpResponseMixin, View):
    # @Override
    def get(self, request, *args, **kwargs):
        try:
            posts = Post.objects.all()
            eserializer = PostSerializer(posts, many=True)
            print('===========')
            print(eserializer.data)
            print('===========')
            json_data = JSONRenderer().render(eserializer.data)
        except Post.DoesNotExist:
            json_data = json.dumps({'msg': 'The requested resource is not available'})
            return self.render_to_http_response(json_data, 400)
        else:
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