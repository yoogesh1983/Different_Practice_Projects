from django.urls import path, re_path

from twmwebservice import views
from twmwebservice import classBasedViews as cbv

urlpatterns = [
    path('post/', views.getpost),
    path('cbv/post/', cbv.PostListCBV.as_view()),
    re_path('cbv/post/(?P<id>\d+)/$', cbv.PostDetailCBV.as_view()),
    ]