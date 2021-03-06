import datetime
import json

from django.http import HttpResponse
from django.utils import timezone
from twmblog.models import Post

"""
 What is Mixin?
 => A class which acts as parent class to provide functionality to the child class only but doesn't 
    do anything for its own is a mixin. You can think of mixing is a method inside a abstract class.
 => Mixin class always extends Object class and it is a direct parent of object class. You can write all
    the utility methods here and extend class to your own class. Since python supports multiple inheritence
    you are not bound to only one class to extend (unlike java). This is the reason there is no mixin
    concept in java. In Java if we need mixing like functionality we create a util class.
 => Mixin is used for code reusability purpose
"""

#Mixin is a direct child class of Object and it does not extends any other classes
#so either you provide object or not it always extend object class
class HttpResponseMixin(object):

    def render_to_http_response(self, json_data, status=200):
        return HttpResponse(json_data, content_type='application/json', status=status)

    def remove_meta_data(self, json_data):
        list_data = []
        dict_data = json.loads(json_data)
        for obj in dict_data:
            list_data.append(obj['fields'])
        return json.dumps(list_data)

    def get_post_with_id(self, id):
        try:
            post = Post.objects.get(id=id)
        except Post.DoesNotExist:
            post = None
        return post

    def generateRequireFields(self, dict_data):
        dict_data['slug'] = dict_data['title'].replace(" ", "").lower()
        dict_data['publish'] = datetime.datetime.now()
        dict_data['created'] = timezone.now
        dict_data['updated'] = timezone.now
        dict_data['author'] = 1