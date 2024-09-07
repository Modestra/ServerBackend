from django.shortcuts import render
from rest_framework import (status, viewsets)
from solarlabshop.models import *
from solarlabshop.serializers import *
from rest_framework.response import Response

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


