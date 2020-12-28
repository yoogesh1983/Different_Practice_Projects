from django.http import HttpResponse
from django.shortcuts import render

from twmblog.models import Post

def getpost(request):
    post = {
        'title': 'This is title',
        'body' : 'This is body',
    }
    resp = '<h1>Post Title:{} </br> Post Body:{}</h1>'.format(post['title'], post['body'])
    return HttpResponse(resp)
