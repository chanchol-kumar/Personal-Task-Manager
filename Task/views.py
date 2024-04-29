from django.shortcuts import render
from rest_framework import viewsets
from Task.models import TaskModel
from Task.serializers import TaskSerializer

# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):
    queryset = TaskModel.objects.all()
    serializer_class = TaskSerializer
