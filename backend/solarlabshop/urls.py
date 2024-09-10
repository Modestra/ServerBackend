from django.contrib import admin
from django.urls import (path, include)
from rest_framework import (permissions, routers)
from solarlabshop.views import *

app_name="solarlabshop"

router = routers.DefaultRouter()

router.register(r"card", CardApiViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("cards", CardApiViewSet.as_view({'get': 'list'})),
    path("card/create", CardApiViewSet.as_view({'post': 'create'}))
]
