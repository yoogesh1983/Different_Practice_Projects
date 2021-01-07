from django.urls import path, re_path, include
from rest_framework import routers

from twmwebservice.views import api_views as api, fbv_views as fbv, cbv_views as cbv, mixin_views as mixin, viewSet_view as viewset

router = routers.DefaultRouter()
router.register('ymsViewSet', viewset.PostCrudViewUsingViewSet) #Since PostCrudViewUsingViewSet extends ModelViewSet, the base_name is optional
#router.register('ymsViewSet', viewset.PostCrudViewUsingViewSet, base_name='ymsViewSet')

urlpatterns = [

    # fbv_views [Function Based Views]
    path('fbv/post/', fbv.get_post_by_using_function_based_view),

    # Custom ClassBased views [Durga Rest Framework]
    path('cbv/post/', cbv.PostListCBV.as_view()),
    re_path('cbv/post/(?P<id>\d+)/$', cbv.PostDetailCBV.as_view()),

    # Api [API Views]
    #########################

        #Api view (Custom)
        path('drf/custom/', api.PostListAPIView.as_view()),

        #Api view (out of the box) Single
        path('drf/single/', api.PostCreateAPIView_ShortCutWay.as_view()),
        re_path('drf/single/(?P<id>\d+)/$', api.PostRetrieveAPIView_ShortCutWay.as_view()),
        re_path('drf/single/(?P<id>\d+)/$', api.PostUpdateAPIView_ShortCutWay.as_view()),
        re_path('drf/single/(?P<id>\d+)/$', api.PostDestroyAPIView_ShortCutWay.as_view()),

        # Api view (out of the box) Combined
        path('drf/multiple/', api.PostListAndCreateAPIView_ShortCutWay.as_view()),
        #re_path('drf/multiple/(?P<id>\d+)/$', api.PostRetrieveAndUpdateAPIView_ShortCutWay.as_view()),
        #re_path('drf/multiple/(?P<id>\d+)/$', api.PostRetrieveAndDestroyAPIView_ShortCutWay.as_view()),
        re_path('drf/multiple/(?P<id>\d+)/$', api.PostRetrieveUpdateAndDestroyAPIView_ShortCutWay.as_view()),

        # Using Mixin
        path('drf/mixin/single/', mixin.PostListViewMixin.as_view()),
        path('drf/mixin/multiple/', mixin.PostListAndCreateViewMixin.as_view()),
        re_path('drf/mixin/multiple/(?P<pk>\d+)/$', mixin.PostRetrieveUpdateAndDestroyModelMixin.as_view()),

    # Api [ViewSet]
    #########################
    path('yms/', include(router.urls)),

    ]