from rest_framework import serializers
from backend.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'password')

class ShortUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        field = ['username', 'password']