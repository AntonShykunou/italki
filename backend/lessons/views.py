from .models import Lesson, LessonSession
# from rest_framework.viewsets import GenericViewSet
# from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin
from rest_framework.generics import ListAPIView, RetrieveDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import LessonSerializer, LessonSessionSerializer
from users.models import User, Teacher
from .filters import LessonSessionFilterSet


class LessonListView(ListAPIView):
    # queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

    def get_queryset(self):
        id = self.kwargs['id']
        return Lesson.objects.filter(teacher=id).all()


class LessonRetrieveUpdateDestroyView(RetrieveDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonSessionListView(ListAPIView):
    queryset = LessonSession.objects.all()
    serializer_class = LessonSessionSerializer
    filter_backends = [DjangoFilterBackend]
    filter_class = LessonSessionFilterSet

    # def get_queryset(self):
    #     queryset = LessonSession.objects.all()
