from django.shortcuts import render
from .serializers import DiscussionCommentsSerializer, DiscussionSerializer, ReportSerializer
from discussions.models import Discussion, DiscussionComment, DiscussionReport
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from django_filters.rest_framework import DjangoFilterBackend

class DiscussionListView(ListCreateAPIView):
    queryset = Discussion.objects.all()
    serializer_class = DiscussionSerializer

class MyDiscussionsDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Discussion.objects.all()
    serializer_class = DiscussionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user']

class DiscussionDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Discussion.objects.all()
    serializer_class = DiscussionSerializer

class DiscussionCreateView(CreateAPIView):
    queryset = Discussion.objects.all()
    serializer_class = DiscussionSerializer

class DiscussionCommentsCreateView(CreateAPIView):
    serializer_class = DiscussionCommentsSerializer

    def qet_queryset(self):
        user = self.kwargs['id']
        return DiscussionComment.objects.filter(user=id)

class SendReport(CreateAPIView):
    serializer_class = ReportSerializer

    def qet_queryset(self):
        user = self.kwargs['id']
        return DiscussionReport.objects.filter(user=id)




