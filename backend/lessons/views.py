from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django.http import HttpResponse
# from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView, RetrieveAPIView
from django_filters.rest_framework import DjangoFilterBackend
from users.models import User, Teacher
from users.serializers import UserSerializer
from .serializers import LessonSerializer, LessonSessionSerializer
from .filters import LessonSessionFilterSet
from .choices import CHOICES_STATUS
from .models import Lesson, LessonSession
from .permissions import IsApprovedStatus, IsDeclinedlStatus, IsFinishedlStatus
from rest_framework.generics import get_object_or_404


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


class LessonSessionApprovedView(UpdateAPIView):
    queryset = LessonSession.objects.all()
    serializer_class = LessonSessionSerializer
    permission_classes = [IsApprovedStatus]

    def post(self,request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        lessonsession = get_object_or_404(LessonSession.objects.all(), pk=pk)
        self.check_object_permissions(self.request, lessonsession)
        data = {
            'status' : 'approved'
        }
        serializer = LessonSessionSerializer(instance=lessonsession,data=data,partial=True)

        if serializer.is_valid():           
            serializer.save()
            return Response(serializer.data)
        else:
                return Response({"fail":"'{}'".format(serializer.errors)})


class LessonSessionDeclinedView(UpdateAPIView):
    queryset = LessonSession.objects.all()
    serializer_class = LessonSessionSerializer
    permission_classes  = [IsDeclinedlStatus]
   
    def post(self,request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        lessonsession = get_object_or_404(LessonSession.objects.all(), pk=pk)
        self.check_object_permissions(self.request, lessonsession)
        data = {
            'status' : 'declined'
        }
        serializer = LessonSessionSerializer(instance=lessonsession,data=data,partial=True)

        if serializer.is_valid():           
            serializer.save()
            return Response(serializer.data)
        else:
                return Response({"fail":"'{}'".format(serializer.errors)})


class LessonSessionFinishedView(UpdateAPIView):
    queryset = LessonSession.objects.all()
    serializer_class = LessonSessionSerializer
    permission_classes = [IsFinishedlStatus]
    
    def post(self,request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        lessonsession = get_object_or_404(LessonSession.objects.all(), pk=pk)
        self.check_object_permissions(self.request, lessonsession)
        data = {
            'status' : 'finished'
        }
        serializer = LessonSessionSerializer(instance=lessonsession,data=data,partial=True)
        if serializer.is_valid():           
            serializer.save()
            return Response(serializer.data)
        else:
                return Response({"fail":"'{}'".format(serializer.errors)})
    