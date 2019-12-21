from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django.http import HttpResponse
# from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView, RetrieveAPIView
from django_filters.rest_framework import DjangoFilterBackend
from users.models import User, Teacher
from .serializers import LessonSerializer, LessonSessionSerializer
from .filters import LessonSessionFilterSet
from .choices import CHOICES_STATUS
from .models import Lesson, LessonSession
from .permissions import IsApprovedStatus, IsDeclinedlStatus, IsFinishedlStatus
from rest_framework.generics import get_object_or_404

class LessonListView(ListAPIView):
    # queryset = Lesson.objects.all()
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
    permission_class = (IsApprovedStatus,)
    
    def get_object(self, pk):
        try:
            return LessonSession.objects.get(pk=pk)
        except LessonSession.DoesNotExist:
            raise Http404

    def post(self, request, pk):
        photo = self.get_object(pk)
        serializer = UserSerializer(photo, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LessonSessionDeclinedView(UpdateAPIView):
    queryset = LessonSession.objects.all()
    serializer_class = LessonSessionSerializer
    permission_class = (IsDeclinedlStatus,)

    def post(self, request, pk):
        status = 'Declined'
        LessonSession.objects.update(status=status)
        return HttpResponse('Declined', status=201)

class LessonSessionFinishedView(UpdateAPIView):
    queryset = LessonSession.objects.all()
    serializer_class = LessonSessionSerializer
    permission_class = (IsFinishedlStatus,)

    def post(self, request, pk):
        status = 'finished'
        LessonSession.objects.update(status=status)
        return HttpResponse('Finished', status=201)
