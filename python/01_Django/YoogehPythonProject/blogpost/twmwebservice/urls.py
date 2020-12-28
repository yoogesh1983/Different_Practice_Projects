from django.urls import path, re_path

from twmwebservice import views

urlpatterns = [
    path('post/', views.getpost),
]