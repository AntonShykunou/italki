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
        elif 'update' in self.action:
            return UserUpdateSerializer
        else:
            return UserSerializer
    
    def post(self, request, pk, format=None):
        current_user = request.user
        param = request.data
        profile = User.objects.filter(user=current_user.pk)
        if profile:
            serializer = UserUpdateSerializer(profile, many=True)
            return Response(serializer.data)
        else:
            serializer = UserUpdateSerializer(data=param)
            if serializer.is_valid(raise_exception=True):
                serializer.save(user=current_user)
                new_data = serializer.data
                return Response(new_data)
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)