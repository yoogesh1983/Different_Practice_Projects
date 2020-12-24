from django.urls import path, re_path

from YMSBlog import views

urlpatterns = [
    path('home/', views.getAllPost),
    #path('home/', views.getAllPost_ClassBasedView.as_view()),

    # replace id with the number of digits. d+ means digits can be of any numbers. if we don't provide + then it means only one digit
    #[-\w]+ means you can take alphanumeric character any number of times (since post is not digits)
    # $ means do not take anything after id
    re_path('(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$', views.post_detail_view, name='detail'),
]