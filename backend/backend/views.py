from django.shortcuts import render
from .serializers import PersonSerializer
from rest_framework import (generics, status, serializers, viewsets)
from rest_framework.views import APIView
from backend.models import Person
from rest_framework.response import Response


class PersonApiView(viewsets.ModelViewSet):
    """Предоставляет данные к активным пользователям"""
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    http_method_names = ['get']

    def get_queryset(self):
        get_queryset = super().get_queryset()
        person_pk = self.kwargs.get('person_pk')
        return get_queryset

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

class TestApiView(APIView):
    def get(self, request):
        el = Person.objects.all().values()
        return Response({'users': list(el)})
    def post(self, request):
        return Response({'title': 'Jennifer Shrader Lawrence'})
        