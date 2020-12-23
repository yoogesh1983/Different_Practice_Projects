import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

from . import forms
from YMSBlog.models import Post

def getAllPost(request):
    blogs = Post.objects.all()
    ctx = {'blogs': blogs}
    return render(request, 'blog/home.html', ctx)

def post_detail_view(request, year, month, day, post):
    ###### Both below are same ######
    #employee = Employee.objects.get(firstName__eq='yoogesh')
    #employee = get_object_or_404(Employee, firstName='yoogesh')
    post=get_object_or_404(Post, slug=post, status='published', publish__year=year, publish__month=month, publish__day= day)
    ctx = {'post': post}
    return render(request, 'blog/detail.html', ctx)