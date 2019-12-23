from django.shortcuts import render
from .models import User
from .serializers import UserSerializer, UserCreateSerializer, UserUpdateSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import FormParser, FileUploadParser, MultiPartParser
from rest_framework.decorators import action

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'create':
            return UserCreateSerializer
        elif 'update' in self.action:
            return UserUpdateSerializer
        else:
            return UserSerializer
    
    
class UploadPhotoView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def put(self, request, *args, **kwargs):
        file_serializer = UserUpdateSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data)
        else:
            return Response(file_serializer.errors)