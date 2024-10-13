from django.urls import (path, include)
from Vasiliq.views import *

urlpatterns = [
    path('client', ClientApiViewSet.as_view({"get": "list"})),
    path('client/create', ClientApiViewSet.as_view({"post": "create"})),
    path('medical', MedicalApiViewSet.as_view({"get": "list"})),
    path('medical/create', MedicalApiViewSet.as_view({"post": "create"})),
    path('history', HistoryApiViewSet.as_view({"get": "list"})),
    path('history/create', HistoryApiViewSet.as_view({"post": "create"})),
    path('admin', AdminApiViewSet.as_view({"get": "list"})),
    path('admin/create', AdminApiViewSet.as_view({"post": "create"})),
    path('order', OrderApiViewSet.as_view({"get": "list"})),
    path('order/create', OrderApiViewSet.as_view({"post": "create"})),
]
