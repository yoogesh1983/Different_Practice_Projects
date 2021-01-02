import json

import requests
from django.core.serializers import serialize
from django.http import HttpResponse
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