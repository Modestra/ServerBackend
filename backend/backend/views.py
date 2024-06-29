from django.shortcuts import render
from .serializers import UserSerializer
from rest_framework import (generics, status, serializers, viewsets)
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from backend.models import User
from rest_framework.response import Response


class PersonApiView(viewsets.ModelViewSet):
    """Предоставляет данные к активным пользователям"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get']

    def get_queryset(self):
        get_queryset = super().get_queryset()
        person_pk = self.kwargs.get('person_pk')
        return get_queryset

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

class TestApiView(APIView):
    def get(self, request):
        el = User.objects.all().values()
        return Response({'users': list(el)})
    def post(self, request):
        return Response({'title': 'Jennifer Shrader Lawrence'})

class RegisterApiView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serialize = UserSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': "Пользователь не зарегистрирован"}, status=status.HTTP_401_UNAUTHORIZED)
        