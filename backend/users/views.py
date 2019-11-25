from django.shortcuts import render
from .models import User
from .serializers import UserSerializer, UserCreateSerializer
from rest_framework import viewsets
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_classes = {
        'list': UserSerializer,
        'get': UserSerializer,
        'create': UserCreateSerializer,
        'update': UserSerializer
    }

    
    def get_serializer_class(self):
        if self.action == 'create':
            return UserCreateSerializer
        else:
            return UserSerializer