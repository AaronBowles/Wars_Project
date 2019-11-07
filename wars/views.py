from django.shortcuts import render
from rest_framework import generics

from .serializers import WarSerializer
from .models import War
# Create your views here.

class WarList(generics.ListCreateAPIView):
    queryset = War.objects.all()
    serializer_class = WarSerializer

class WarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = War.objects.all()
    serializer_class = WarSerializer