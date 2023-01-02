from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import student
from .serializers import StudentSerializer

class studlist(generics.ListCreateAPIView):
    queryset = student.objects.all()
    serializer_class = StudentSerializer


class studDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset =student.objects.all()
    serializer_class = StudentSerializer
    