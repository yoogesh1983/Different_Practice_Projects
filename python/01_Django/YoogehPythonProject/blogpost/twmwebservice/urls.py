from django.urls import path, re_path

from twmwebservice.views import api_views as api, fbv_views as fbv, custom_views as custom

urlpatterns = [
    #Function based view
    path('fbv/post/', fbv.get_post_by_using_function_based_view),

    # Class based view
    path('cbv/post/', custom.PostListCBV.as_view()),
    re_path('cbv/post/(?P<id>\d+)/$', custom.PostDetailCBV.as_view()),

     #path('drf/', api.PostCreateAPIView_ShortCutWay.as_view()),
    # re_path('drf/(?P<id>\d+)/$', api.PostRetrieveAPIView_ShortCutWay.as_view()),
    # re_path('drf/(?P<id>\d+)/$', api.PostUpdateAPIView_ShortCutWay.as_view()),
    # re_path('drf/(?P<id>\d+)/$', api.PostDestroyAPIView_ShortCutWay.as_view()),

     path('drf/', api.PostListAndCreateAPIView_ShortCutWay.as_view()),
     # re_path('drf/(?P<id>\d+)/$', api.PostRetrieveAndUpdateAPIView_ShortCutWay.as_view()),
     #re_path('drf/(?P<id>\d+)/$', api.PostRetrieveAndDestroyAPIView_ShortCutWay.as_view()),
    #re_path('drf/(?P<id>\d+)/$', api.PostRetrieveUpdateAndDestroyAPIView_ShortCutWay.as_view()),

    ]