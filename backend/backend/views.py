from django.shortcuts import render
from .serializers import PersonSerializer
from rest_framework import viewsets
from backend.models import Person
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(["GET"])
def get_person(request):
    person = Person.objects.all()
    context = {"Person": person}
    return Response(person)

class PersonView(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    http_method_names = ['get']


        