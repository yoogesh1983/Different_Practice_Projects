from django.urls import path
from twmprofile import views

urlpatterns = [
    path('profile/', views.getProfile),
]