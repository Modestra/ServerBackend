from .serializers import (UserSerializer, ShortUserSerializer)
from rest_framework import (status, viewsets)
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import action
from backend.models import *
from rest_framework.response import Response
        
class AuthViewSet(viewsets.ModelViewSet): 
    """Логика авторизации пользователя во встроенную библиотеку авторизации"""
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def list(self, request, *args, **kwargs):
        users = self.get_queryset()
        serializer = self.get_serializer(users, many=True)
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"server": "None"}, status=status.HTTP_400_BAD_REQUEST)