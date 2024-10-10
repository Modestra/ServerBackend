from django.contrib import admin
from django.urls import (path, include)
from rest_framework import (permissions, routers)
from solarlabshop.views import *

app_name="solarlabshop"

router = routers.DefaultRouter()
router.register(r'category', CategoryApiViewSet)
router.register(r'advert', AdvertApiViewSet)
router.register(r'image', ImagesApiViewSet)
router.register(r'comment', CommentApiViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('advert/', AdvertApiViewSet.as_view({'get': 'list'})),
    path('advert/create', AdvertApiViewSet.as_view({'post': 'create'})),
    path('advert/user', AdvertApiViewSet.as_view({"get": "get_by_id"})),
    path('categories/', CategoryApiViewSet.as_view({"get": "list"})),
    path('categories/create', CategoryApiViewSet.as_view({'post': 'create'})),
    #path('categories/childs', CategoryApiViewSet.as_view({'get': 'childs'})),
    path('categories/create/child', CategoryApiViewSet.as_view({'post': 'child'})),
    path('images/', ImagesApiViewSet.as_view({'get': 'list'})),
    path('images/create', ImagesApiViewSet.as_view({'post': 'create'})),
    path('comments/', CommentApiViewSet.as_view({'get': 'childs'}))
]
