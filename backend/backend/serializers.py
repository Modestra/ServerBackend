from rest_framework import serializers
from backend.models import Person

class PersonSerializer(serializers.ListSerializer):
    class Meta:
        model = Person
        field = ['name', 'age']