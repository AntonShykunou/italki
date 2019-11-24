from django.shortcuts import render
from rest_framework import status, permissions
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin
from rest_framework.response import Response
from .models import Language, LearningLanguage
from .serializers import LanguageSerializer, LearningLanguageSerializer


class LanguageViewSet( ListModelMixin,
                        CreateModelMixin,
                        RetrieveModelMixin,
                        GenericViewSet):

    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class LearningLanguageViewSet(  ListModelMixin,
                                CreateModelMixin,
                                RetrieveModelMixin,
                                GenericViewSet):

    queryset = LearningLanguage.objects.all()
    serializer_class = LearningLanguageSerializer
