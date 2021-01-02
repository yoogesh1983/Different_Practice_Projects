import json

import requests
from django.core.serializers import serialize
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import View
from twmwebservice.mixin import HttpResponseMixin
from twmblog.models import Post


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

#@method_decorator(csrf_exempt, name='dispatch') # dispacth means it is applicable to all methods inside this class.
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
        json_data = json.dumps({'msg': 'Hi this is post message'})
        return self.render_to_http_response(json_data)