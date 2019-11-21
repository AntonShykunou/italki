import datetime
from django.shortcuts import render
from feedbacks.models import Feedback
from users.models import User, Teacher
from .serializer import FeedbackSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

class FeedbackCreateView(ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    #permission_classes = [IsAdminUser]

    def list(self, request):
        queryset = self.get_queryset()
        serializer = FeedbackSerializer(queryset, many=True)
        return Response(serializer.data)

class FeedbackDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
# Create your views here.
