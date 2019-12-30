from django.shortcuts import render
from .models import User, Teacher
from .serializers import UserSerializer, UserCreateSerializer, UserUpdateSerializer, TeacherSerializer
from rest_framework import viewsets,generics, mixins, views
from rest_framework.response import Response
from django_filters import rest_framework as filters
from .pagination import StandardResultsSetPagination
from .filters import TeacherFilterSet


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'create':
            return UserCreateSerializer
        elif 'update' in self.action:
            return UserUpdateSerializer
        else:
            return UserSerializer


class TeacherViewSet(
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     mixins.ListModelMixin,
                     viewsets.GenericViewSet):
    queryset = Teacher.objects.all()\
        .prefetch_related('user')\
        .prefetch_related(
            'user__native_languages',
            'user__communication_tool',
            'user__learning_languages'
        )
    serializer_class = TeacherSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = TeacherFilterSet




