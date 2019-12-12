from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
# from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin
from rest_framework.generics import ListAPIView, UpdateRetrieveDestroy
from django_filters.rest_framework import DjangoFilterBackend
from users.models import User, Teacher
from .serializers import LessonSerializer, LessonSessionSerializer
from .filters import LessonSessionFilterSet
from .choices import CHOICES_STATUS
from .models import Lesson, LessonSession
from rest_framework.permissions import BasePermission


class LessonListView(ListAPIView):
    # queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

    def get_queryset(self):
        id = self.kwargs['id']
        return Lesson.objects.filter(teacher=id).all()


class LessonRetrieveUpdateRetrieveDestroyView(UpdateRetrieveDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonSessionViewSet(ViewSet):
    queryset = LessonSession.objects.all()
    serializer_class = LessonSessionSerializer
    filter_backends = [DjangoFilterBackend]
    filter_class = LessonSessionFilterSet

class LessonSessionApprovedView():
    pass

class LessonSessionDeclinedView():
    pass

class LessonSessionFinishedView():
    pass
    # @action(method=['patch'], detail=True, )
    # def change_status(self, request):
    #     if CHOISES_STATUSE[0]
    # # def get_queryset(self):
    # #     queryset = LessonSession.objects.all()
