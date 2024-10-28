from .serializers import (UserSerializer, ShortUserSerializer)
from rest_framework import (status, viewsets)
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
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
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"server": "Форма не валидна. Недостаточно данных"}, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=["POST"])
    def user_login(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"token": user.token, "user_id": user.user_id}, status=status.HTTP_201_CREATED)
        return Response({"error": "Не удалось получить данные пользователя"}, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=["GET"])
    def get_token(self, request):
        data = request.GET.get('email', "default")
        user = User.objects.get(email=data)
        return Response({"token": user.token}, status=status.HTTP_200_OK)