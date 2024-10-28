from django.shortcuts import render
from rest_framework import (status, viewsets)
from solarlabshop.models import *
from solarlabshop.serializers import *
from rest_framework.response import Response
from rest_framework.decorators import action, api_view
from rest_framework.permissions import IsAuthenticated, AllowAny
from backend.models import User
from backend.serializers import UserSerializer
import json

class CategoryApiViewSet(viewsets.ModelViewSet):

    queryset = Categories.objects.all()
    serializer_class = CategorySerializer

    def list(self, request, *args, **kwargs):
        category_id = request.GET.get("id", "3fa85f64-5717-4562-b3fc-2c963f66afa6")
        category_list = Categories.objects.filter(parentid=category_id)
        serializer = CategorySerializer(category_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=["POST"])
    def child(self, request):
        serializer = CategoryChildSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            category = Categories.objects.get(name=request.data["name"])
            return Response({"userid": category.category_id, "name": category.name, "parentid": category.parentid}, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

class AdvertApiViewSet(viewsets.ModelViewSet):

    queryset = Advert.objects.all()
    serializer_class = AdvertSerializer
    permission_classes = (AllowAny, IsAuthenticated)
    
    def check_permissions(self, request):
        return super().check_permissions(request)

    def list(self, request, *args, **kwargs):
        name = request.GET.get('name', "")
        adverts = Advert.objects.filter(name=name)
        serializer = AdvertSerializer(adverts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"error": "Невалидный запрос"}, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=["GET"])
    def get_by_id(self, request):
        user_id = request.GET.get("id", "3fa85f64-5717-4562-b3fc-2c963f66afa6")
        adverts = Advert.objects.filter(user_id=user_id)
        serializer = AdvertSerializer(adverts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class ImagesApiViewSet(viewsets.ModelViewSet):

    queryset = Images.objects.all()
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
        advert_id = request.GET.get("id", "3fa85f64-5717-4562-b3fc-2c963f66afa6")
        comments = Comments.objects.filter(advert_id=advert_id)
        serializer = self.get_serializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

