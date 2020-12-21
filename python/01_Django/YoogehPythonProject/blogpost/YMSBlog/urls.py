from django.urls import path, re_path

from YMSBlog import views

urlpatterns = [
    path('home/', views.getAllPost),
]