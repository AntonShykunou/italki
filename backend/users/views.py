from django.shortcuts import render
from .models import User
from .serializers import UserSerializer, UserCreateSerializer, UserUpdateSerializer
from rest_framework import viewsets
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'create':
            return UserCreateSerializer
        elif self.action == 'update':
            return UserUpdateSerializer
        else:
            return UserSerializer