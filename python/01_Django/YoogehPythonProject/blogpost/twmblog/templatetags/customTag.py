from django import template
from twmblog.models import Post
from django.db.models import Count

register = template.Library()

@register.filter(name='ymsTruncate5')
def truncate5(input):
    return input[0:5]

@register.filter(name='ymsTruncateN')
def truncateN(input, number):
    return input[0:number]

#simple_tag perform some processing and returns a string
@register.simple_tag(name='ymsTotalPostCount')
def totalPosts():
    return Post.objects.count();

#inclusion_tag perform some processing and returns a rendered template
@register.inclusion_tag('blog/latestPost.html')
def getLatestPosts(count=3):
    latest_posts = Post.objects.order_by('-publish')[:count]
    return {'latest_posts' : latest_posts}

#assignment_tag perform some procesing and assign result to the variable in the context so that we can use that veriable anywhere
#However it is deprecated since simple tag is enough to do it from django 1.9 onwards
#@register.assignment_tag
@register.simple_tag
def getMostCommentedPosts(count=3):
    return Post.objects.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]



#registering our custom filter into a template filter (if you do not provide the annotation)
#register.filter('ymsTruncate5', truncate5)
#register.filter('ymsTruncateN', truncateN)
