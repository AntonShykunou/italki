from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.generics import (ListAPIView, RetrieveUpdateDestroyAPIView, 
                                    UpdateAPIView, RetrieveAPIView
                                    )
from django_filters.rest_framework import DjangoFilterBackend
from users.models import User, Teacher
from users.serializers import UserSerializer
from .serializers import LessonSerializer, LessonSessionSerializer
from .filters import LessonSessionFilterSet
from .choices import CHOICES_STATUS
from .models import Lesson, LessonSession
from .permissions import CanApproveLessonSession, CanDeclinedLessonSession, CanFinishLessonSession
from rest_framework.generics import get_object_or_404
from .services import approve_lesson_session, decline_lesson_session, finish_lesson_session


class LessonListView(ListAPIView):
    serializer_class = LessonSerializer

    def get_queryset(self):
        id = self.kwargs['id']
        return Lesson.objects.filter(teacher=id).all()


class LessonRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonSessionView(ListAPIView):
    queryset = LessonSession.objects.all()
    serializer_class = LessonSessionSerializer
    filter_backends = [DjangoFilterBackend]
    filter_class = LessonSessionFilterSet


class LessonSessionDetailView(RetrieveAPIView):
    queryset = LessonSession.objects.all()
    serializer_class = LessonSessionSerializer


class LessonSessionApproveView(UpdateAPIView):
    queryset = LessonSession.objects.all()
    serializer_class = LessonSessionSerializer
    permission_classes = [CanApproveLessonSession]

    def post(self,request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        lessonsession = get_object_or_404(LessonSession.objects.all(), pk=pk)
        self.check_object_permissions(self.request, lessonsession)
        approve_lesson_session(lessonsession)
        return HttpResponse('Lesson session approved')


class LessonSessionDeclineView(UpdateAPIView):
    queryset = LessonSession.objects.all()
    serializer_class = LessonSessionSerializer
    permission_classes  = [CanDeclinedLessonSession]
   
    def post(self,request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        lessonsession = get_object_or_404(LessonSession.objects.all(), pk=pk)
        self.check_object_permissions(self.request, lessonsession)
        decline_lesson_session(lessonsession)
        return HttpResponse('Lesson session declined')


class LessonSessionFinishView(UpdateAPIView):
    queryset = LessonSession.objects.all()
    serializer_class = LessonSessionSerializer
    permission_classes = [CanFinishLessonSession]
    
    def post(self,request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        lessonsession = get_object_or_404(LessonSession.objects.all(), pk=pk)
        self.check_object_permissions(self.request, lessonsession)
        finish_lesson_session(lessonsession)
        return HttpResponse('Lesson session finished')
    