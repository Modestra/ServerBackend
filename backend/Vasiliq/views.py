from django.shortcuts import render
from rest_framework import (status, viewsets)
from Vasiliq.models import *
from Vasiliq.serializers import *

class ClientApiViewSet(viewsets.ModelViewSet):
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
