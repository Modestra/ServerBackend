from django.shortcuts import render
from rest_framework import (status, viewsets)
from solarlabshop.models import *
from solarlabshop.serializers import *
from rest_framework.response import Response
from rest_framework.decorators import action, api_view
from rest_framework.permissions import IsAuthenticated, AllowAny
from solarlabshop.models import User as SolarUser
from django.http import QueryDict
import json

class CategoryApiViewSet(viewsets.ModelViewSet):

    queryset = Categories.objects.all()
    serializer_class = CategorySerializer

    @action(detail=True, methods=["GET"])
    def childs(self, request, *args, **kwargs):
        category_id = request.GET.get("id", "579a1ed96a0f48f2b6262e9dcfdec242")
        category_list = Categories.objects.filter(parentid=category_id)
        serializer = CategorySerializer(category_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

class AuthApiViewSet(viewsets.ModelViewSet):

    queryset = SolarUser.objects.all()
    serializer_class = AuthSerializer
    permission_classes = [AllowAny]
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = SolarUser.objects.get(email=request.data["email"])
            return Response({"user": serializer.data, "token": user.token}, status=status.HTTP_201_CREATED) #Работает, если пользователь не создан
        return Response({"error": "Было создано несколько пользователей с данным email или username"}, status=status.HTTP_400_BAD_REQUEST)
        #return Response({"error": "Не удалось создать пользователя"}, status=status.HTTP_400_BAD_REQUEST)
    @action(detail=False, methods=["POST"] ,permission_classes=[AllowAny])
    def user_login(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = SolarUser.objects.get(username=request.data["username"])
            return Response({"token": user.token}, status=status.HTTP_201_CREATED)
        return Response({"error": "Не удалось получить данные пользователя"}, status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @action(detail=True, methods=["GET"])
    def get_token(self, request):
        data = request.GET.get('email', "default")
        user = SolarUser.objects.get(email=data)
        return Response({"token": user.token}, status=status.HTTP_200_OK)
    
class AdvertApiViewSet(viewsets.ModelViewSet):

    queryset = Advert.objects.all()
    serializer_class = AvitoSerializer

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    
class ImagesApiViewSet(viewsets.ModelViewSet):

    queryset = Categories.objects.all()
    serializer_class = ImageSerializer

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

class CommentApiViewSet(viewsets.ModelViewSet):

    queryset = Comments.objects.all()
    serializer_class = CommentSerializer

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @action(detail=False, methods=["GET"])
    def childs(self, request):
        pass

