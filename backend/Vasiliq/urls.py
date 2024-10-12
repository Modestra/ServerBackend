from django.urls import (path, include)
from Vasiliq.views import *

urlpatterns = [
    path('client', ClientApiViewSet.as_view({"get": "list"})),
    path('client/create', ClientApiViewSet.as_view({"post": "create"})),
]
