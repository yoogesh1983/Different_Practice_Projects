from django.urls import path, re_path

from twmwebservice import views

urlpatterns = [
    #Function based view
    path('fbv/post/', views.get_post_by_using_function_based_view),

    # Class based view
    path('cbv/post/', views.PostListCBV.as_view()),
    re_path('cbv/post/(?P<id>\d+)/$', views.PostDetailCBV.as_view()),

    # DRF (Django Rest Framework)
    path('drf/post/', views.PostListDRF.as_view()),
    re_path('drf/post/(?P<id>\d+)/$', views.PostDetailDRF.as_view()),
    ]