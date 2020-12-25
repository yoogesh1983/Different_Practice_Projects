import datetime

from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from taggit.models import Tag

from . import forms
from YMSBlog.models import Post

from .forms import EmailSendRequest, CommentRequest


def getAllPost(request, tag_slug=None):
    blogs = Post.objects.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        blogs = blogs.filter(tags__in=[tag])

    paginator = Paginator(blogs, 4)  # how many results in one page you want to display?
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

    ctx = {'blogs': blogs, 'classBasedView': True, 'tag': tag}
    return render(request, 'blog/home.html', ctx)


def getPostDetail(request, year, month, day, post):
    ###### Both below are same ######
    # employee = Employee.objects.get(firstName__eq='yoogesh')
    # employee = get_object_or_404(Employee, firstName='yoogesh')
    post = get_object_or_404(Post, slug=post, status='published', publish__year=year, publish__month=month,
                             publish__day=day)

    # We have specified related_name='comments' in models.py file and this is why we can use post.comments
    allComments = post.comments.filter(active=True)
    submitted = False
    if request.method == 'POST':
        form = CommentRequest(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            submitted = True
    else:
        form = CommentRequest()

    ctx = {'post': post, 'comments': allComments, 'submitted': submitted, 'form': form}
    return render(request, 'blog/detail.html', ctx)


class getAllPost_ClassBasedView(ListView):
    model = Post
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
            cd = form.cleaned_data
            name = cd['name']
            toEmail = cd['to']
            subject = '{} ({}) recommends you to read about "{}"!!'.format(name, cd['email'], post.title)
            msg = 'Read Post At:\n {} \n\n{}\'s Comments:\n{}'.format(
                request.build_absolute_uri(post.get_absolute_url()), name, cd['comments'])

            # Send Email
            send_mail(subject, msg, 'donotReply@gmail.com', [toEmail])

            form = EmailSendRequest()
            ctx = {'name': toEmail, 'post': post, 'form': form}
        else:
            ctx = {'form': form, 'post': post}
    elif request.method == 'GET':
        form = EmailSendRequest();
        ctx = {'form': form, 'post': post}

    response = render(request, redirecturl, ctx)
    return response
