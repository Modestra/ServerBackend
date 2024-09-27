from django.shortcuts import render
from rest_framework import (status, viewsets)
from solarlabshop.models import *
from solarlabshop.serializers import *
from rest_framework.response import Response
from rest_framework.decorators import action, api_view
from solarlabshop.models import User as SolarUser
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.http import QueryDict
import json

class CardApiViewSet(viewsets.ModelViewSet):

    queryset = Card.objects.all()
    serializer_class = CardSerializer

    def list(self, request, *args, **kwargs):
        users = self.get_queryset()
        serializer = self.get_serializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

class AuthApiViewSet(viewsets.ModelViewSet):

    queryset = SolarUser.objects.all()
    serializer_class = AuthSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = SolarUser.objects.get(email=request.data["email"])
            return Response({"user": serializer.data, "token": user.token}, status=status.HTTP_201_CREATED) #Работает, если пользователь не создан
        return Response({"error": "Было создано несколько пользователей с данным email"}, status=status.HTTP_400_BAD_REQUEST)
        #return Response({"error": "Не удалось создать пользователя"}, status=status.HTTP_400_BAD_REQUEST)
    @action(detail=False, methods=["POST"])
    def user_login(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = SolarUser.objects.get(username=request.data["username"])
            return Response({"token": user.token}, status=status.HTTP_201_CREATED)
        return Response({"error": "Не удалось получить данные пользователя"}, status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

