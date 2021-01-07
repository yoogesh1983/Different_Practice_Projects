from django.urls import path, re_path

from twmwebservice import views

urlpatterns = [
    #Function based view
    path('fbv/post/', views.get_post_by_using_function_based_view),

    # Class based view
    path('cbv/post/', views.PostListCBV.as_view()),
    re_path('cbv/post/(?P<id>\d+)/$', views.PostDetailCBV.as_view()),

    # path('drf/', views.PostCreateAPIView_ShortCutWay.as_view()),
    # re_path('drf/(?P<id>\d+)/$', views.PostRetrieveAPIView_ShortCutWay.as_view()),
    # re_path('drf/(?P<id>\d+)/$', views.PostUpdateAPIView_ShortCutWay.as_view()),
    # re_path('drf/(?P<id>\d+)/$', views.PostDestroyAPIView_ShortCutWay.as_view()),

    # path('drf/$', views.PostListAndCreateAPIView_ShortCutWay.as_view()),
    # re_path('drf/(?P<id>\d+)/$', views.PostRetrieveAndUpdateAPIView_ShortCutWay.as_view()),
    # re_path('drf/(?P<id>\d+)/$', views.PostRetrieveAndDestroyAPIView_ShortCutWay.as_view()),
    re_path('drf/(?P<id>\d+)/$', views.PostRetrieveUpdateAndDestroyAPIView_ShortCutWay.as_view()),

    ]