from rest_framework import serializers
from backend.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        field = ['username', 'age', 'userage', 'email', 'password']

class ShortUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        field = ['username', 'password']