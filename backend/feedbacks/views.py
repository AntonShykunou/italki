import datetime
from django.shortcuts import render
from feedbacks.models import Feedback
from users.models import User, Teacher
from .serializer import FeedbackSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser


class FeedbackListView(ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    #permission_classes = [IsAdminUser]


class FeedbackDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
# Create your views here.
