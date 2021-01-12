from django.urls import path, re_path, include
from rest_framework import routers
from rest_framework.authtoken import views as token
from rest_framework_jwt import views as jwt
from twmwebservice.views import api_views_ootb as apiootb, fbv_views as fbv, cbv_views as cbv, mixin_views as mixin, viewSet_view as viewset, api_views_core as apicore

router = routers.DefaultRouter()
router.register('ymsViewSet', viewset.PostCrudViewUsingViewSet) #Since PostCrudViewUsingViewSet extends ModelViewSet, the base_name is optional
#router.register('ymsViewSet', viewset.PostCrudViewUsingViewSet, base_name='ymsViewSet')

urlpatterns = [

   # For JWT token
    path('jwt-access-token/', jwt.obtain_jwt_token, name='get-access-token'),
    path('jwt-refresh-token/', jwt.refresh_jwt_token, name='get-refresh-token'),
    path('jwt-validate-token/', jwt.verify_jwt_token, name='verify-token'),



    # For DRF Authtoken
    path('token/', token.obtain_auth_token, name='get-my-token'),

    # fbv_views [Function Based Views]
    path('fbv/post/', fbv.get_post_by_using_function_based_view),

    # Custom ClassBased views [Durga Rest Framework]
    path('cbv/post/', cbv.PostListCBV.as_view()),
    re_path('cbv/post/(?P<id>\d+)/$', cbv.PostDetailCBV.as_view()),

    # Api [API Views]
    #########################

        #Api view (core)
        path('drf/apiviews/core/', apicore.PostListAPIViewFor_Get_GetAll_and_Post.as_view()),
        re_path('drf/apiviews/core/(?P<id>\d+)/$', apicore.PostListAPIViewFor_Get_Put_Patch_and_Delete.as_view()),

        #Api view (out of the box) Single
        re_path('drf/apiviews/ootb/single/(?P<id>\d+)/$', apiootb.PostRetrieveAPIView_ShortCutWay.as_view()),
        re_path('drf/apiviews/ootb/single/ootb/', apiootb.PostListAPIView_ShortCutWay.as_view()),
        path('drf/apiviews/ootb/single/', apiootb.PostCreateAPIView_ShortCutWay.as_view()),
        re_path('drf/apiviews/ootb/single/(?P<id>\d+)/$', apiootb.PostUpdateAPIView_ShortCutWay.as_view()),
        re_path('drf/apiviews/ootb/single/(?P<id>\d+)/$', apiootb.PostDestroyAPIView_ShortCutWay.as_view()),

        # Api view (out of the box) Combined
        path('drf/multiple/', apiootb.PostListAndCreateAPIView_ShortCutWay.as_view()),
        #re_path('drf/multiple/(?P<id>\d+)/$', api.PostRetrieveAndUpdateAPIView_ShortCutWay.as_view()),
        #re_path('drf/multiple/(?P<id>\d+)/$', api.PostRetrieveAndDestroyAPIView_ShortCutWay.as_view()),
        re_path('drf/multiple/(?P<id>\d+)/$', apiootb.PostRetrieveUpdateAndDestroyAPIView_ShortCutWay.as_view()),

        # Using Mixin
        path('drf/mixin/single/', mixin.PostListViewMixin.as_view()),
        path('drf/mixin/multiple/', mixin.PostListAndCreateViewMixin.as_view()),
        re_path('drf/mixin/multiple/(?P<pk>\d+)/$', mixin.PostRetrieveUpdateAndDestroyModelMixin.as_view()),

    # Api [ViewSet]
    #########################
    path('yms/', include(router.urls)),

    ]