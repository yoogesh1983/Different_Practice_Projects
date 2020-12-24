import datetime

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView

from . import forms
from YMSBlog.models import Post

from .forms import EmailSendRequest


def getAllPost(request):
    blogs = Post.objects.all()

    paginator = Paginator(blogs, 2) # how many results in one page you want to display?
    pageNumber = request.GET.get('page')
    try:
        blogs = paginator.page(pageNumber)
    except PageNotAnInteger:
        # This is the handle the homepage scenario where we don't pass ?page=1
        blogs = paginator.page(1)
    except EmptyPage:
        # display the last page is no results found
        # This happens if somebody passes ?page=200 in a request url
        blogs = paginator.page(paginator.num_pages)

    ctx = {'blogs': blogs, 'classBasedView': True}
    return render(request, 'blog/home.html', ctx)

def getPostDetail(request, year, month, day, post):
    ###### Both below are same ######
    #employee = Employee.objects.get(firstName__eq='yoogesh')
    #employee = get_object_or_404(Employee, firstName='yoogesh')
    post=get_object_or_404(Post, slug=post, status='published', publish__year=year, publish__month=month, publish__day= day)
    ctx = {'post': post}
    return render(request, 'blog/detail.html', ctx)

class getAllPost_ClassBasedView(ListView):
    model=Post
    paginate_by = 2
    template_name = 'blog/home.html'
    context_object_name = 'blogs'

def sendMail(request, id):
    post = get_object_or_404(Post, id=id, status='published')
    redirecturl = 'blog/email.html'
    ctx = ''

    if request.method == 'POST':
        # handling form submission scenario
        form = EmailSendRequest(request.POST)
        if form.is_valid():
            cleanedData = form.cleaned_data
            toEmail = form.cleaned_data['to']
            form = EmailSendRequest()
            ctx = {'name': toEmail, 'post': post, 'form': form}
        else:
            ctx = {'form': form, 'post': post}
    elif request.method == 'GET':
        form = EmailSendRequest();
        ctx = {'form': form, 'post': post}

    response = render(request, redirecturl, ctx)
    return response

