from django.shortcuts import render
from rest_framework import (viewsets)
from RedOx.models import Notes

class NoteApiView(viewsets.ModelViewSet):
    queryset = Notes.objects.all()
    class Meta:
        model = Notes
