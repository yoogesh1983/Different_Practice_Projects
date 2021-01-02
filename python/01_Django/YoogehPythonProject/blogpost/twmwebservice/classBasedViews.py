import json

import requests
from django.contrib.auth.models import User
from django.core.serializers import serialize
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import View
from twmwebservice.mixin import HttpResponseMixin
from twmblog.models import Post

from twmwebservice import twmUtil
from twmblog.forms import AddPostRequest


class PostDetailCBV(HttpResponseMixin, View):
    #@Override
    def get(self, request, id, *args, **kwargs):
        try:
            post = Post.objects.get(id=id)
        except Post.DoesNotExist:
            json_data = json.dumps({'msg': 'The requested resource is not available'})
            return self.render_to_http_response(json_data, 400)
        else:
            json_data = self.remove_meta_data(serialize('json', [post, ]))  # Serialize() method required list as argument
            return self.render_to_http_response(json_data)

# dispacth means it is applicable to all methods inside this class.
# If you want to exempt only a post metod then you can do name='post'
@method_decorator(csrf_exempt, name='dispatch')
class PostListCBV(HttpResponseMixin, View):
    #@Override
    def get(self, request, *args, **kwargs):
        try:
            posts= Post.objects.all()
        except Post.DoesNotExist:
            json_data = json.dumps({'msg': 'The requested resource is not available'})
            return self.render_to_http_response(json_data, 400)
        else:
            json_data = self.remove_meta_data(serialize('json', posts, fields=('title', 'slug')))
            return self.render_to_http_response(json_data)

    #@Override
    @csrf_exempt
    def post(self, request, *args, **kwargs):
        json_data = request.body
        valid_json = twmUtil.is_valid_json(json_data)
        if not valid_json:
            json_data = json.dumps({'msg': 'Invalid Json Format!'})
            return self.render_to_http_response(json_data, 400)

        dict_data= json.loads(json_data)
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