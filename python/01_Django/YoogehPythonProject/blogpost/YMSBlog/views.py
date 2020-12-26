from YMSBlog.models import Post
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template.response import TemplateResponse
from django.views.generic import ListView
from taggit.models import Tag

from .forms import EmailSendRequest, CommentRequest, AddUserRequest, AddPostRequest

def getAllPost(request, tag_slug=None):
    user = request.user
    blogs = Post.objects.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        blogs = blogs.filter(tags__in=[tag])

    paginator = Paginator(blogs, 3)  # how many results in one page you want to display?
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
    return TemplateResponse(request, 'blog/home.html', ctx)


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
    return TemplateResponse(request, 'blog/detail.html', ctx)


class getAllPost_ClassBasedView(ListView):
    model = Post
    paginate_by = 2
    template_name = 'blog/home.html'
    context_object_name = 'blogs'


def sendMail(request, id):
    post = get_object_or_404(Post, id=id, status='published')
    redirecturl = 'blog/email.html'
    form = EmailSendRequest();

    if request.method == 'POST':
        # handling form submission scenario
        form = EmailSendRequest(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            toEmail = cd['to']
            subject = '{} ({}) recommends you to read about "{}"!!'.format(cd['name'], cd['email'], post.title)
            msg = 'Read Post At:\n {} \n\n{}\'s Comments:\n{}'.format(
                request.build_absolute_uri(post.get_absolute_url()), cd['name'], cd['comments'])
            # Send Email
            send_mail(subject, msg, 'donotReply@gmail.com', [toEmail])
            form = EmailSendRequest()
            ctx = {'name': toEmail, 'post': post, 'form': form}
            return render(request, redirecturl, ctx)
    ctx = {'form': form, 'post': post}
    return TemplateResponse(request, redirecturl, ctx)


@login_required
def addUser(request):
    redirecturl = 'blog/admin/admin.html'
    form = AddUserRequest()
    if request.method == 'POST':
        form = AddUserRequest(request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect('/accounts/login')
    ctx = {'form': form}
    return TemplateResponse(request, redirecturl, ctx)


@login_required
def addPost(request):
    redirecturl = 'blog/admin/post.html'
    form = AddPostRequest()
    if request.method == 'POST':
        form = AddPostRequest(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.slug = post.title.lower()
            post.save()
            return HttpResponseRedirect('/')
    ctx = {'form': form}
    return TemplateResponse(request, redirecturl, ctx)
