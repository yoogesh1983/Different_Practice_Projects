from django.urls import path, re_path
from twmprofile import views

urlpatterns = [
    path('profile/', views.getProfile),
    path('admin/', views.getAdminView),

    # replace id with the number of digits. d+ means digits can be of any numbers. if we don't provide + then it means only one digit
    # $ means do not take anything after id
    re_path('deleteProfile/(?P<id>\d+)/$', views.deleteProfile),
    re_path('updateProfile/(?P<id>\d+)/$', views.updateProfile),
]