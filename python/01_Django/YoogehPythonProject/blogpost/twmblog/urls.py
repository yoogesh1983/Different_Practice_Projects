from django.urls import path, re_path

from twmblog import views

urlpatterns = [
    #path('home/', views.getAllPost_ClassBasedView.as_view()),
    path('adduser/', views.addUser),
    path('addpost/', views.addPost),

    re_path('(?P<id>\d+)/share/$', views.sendMail),
    re_path('tag/(?P<tag_slug>[-\w]+)/$', views.getAllPost, name='allPostsByTagName'),

    # replace id with the number of digits. d+ means digits can be of any numbers. if we don't provide + then it means only one digit
    #[-\w]+ means you can take alphanumeric character any number of times (since post is not digits)
    # $ means do not take anything after id
    re_path('(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$', views.getPostDetail, name='detail'),

    #MyWebsite
    path('website/', views.get_my_website),
    path('website/go', views.get_go_lang_website),
]