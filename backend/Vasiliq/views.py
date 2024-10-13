from django.shortcuts import render
from rest_framework import (status, viewsets)
from Vasiliq.models import *
from Vasiliq.serializers import *

class ClientApiViewSet(viewsets.ModelViewSet):
    queryset = Client
    serializer_class = ClientSerializer
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
class AdminApiViewSet(viewsets.ModelViewSet):
    queryset = AdminModel
    serializer_class = AdminSerializer
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
class MedicalApiViewSet(viewsets.ModelViewSet):
    queryset = Medicament
    serializer_class = MedicamentSerializer
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
class OrderApiViewSet(viewsets.ModelViewSet):
    queryset = Order
    serializer_class = OrderSerializer
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

class AdminApiViewSet(viewsets.ModelViewSet):
    queryset = AdminModel
    serializer_class = AdminSerializer
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
class HistoryApiViewSet(viewsets.ModelViewSet):
    queryset = HistoryOrder
    serializer_class = HistorySerializer
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
