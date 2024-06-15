from .serializers import PersonSerializer
from rest_framework import generics
from backend.models import Person

class PersonView(generics.ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
