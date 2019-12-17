from django.shortcuts import render
from .serializers import DiscussionCommentsSerializer, DiscussionSerializer, ReportSerializer
from discussions.models import Discussion, DiscussionComments, DiscussionReport
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView

class DiscussionListView(ListCreateAPIView):
    queryset = Discussion.objects.all()
    serializer_class = DiscussionSerializer

class DiscussionDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = DiscussionSerializer

    def get_queryset(self):
        id = self.kwargs['id']
        return Discussion.objects.filter(author=id)

class DiscussionCreateView(CreateAPIView):
    queryset = Discussion.objects.all()
    serializer_class = DiscussionSerializer

class DiscussionCommentsCreateView(CreateAPIView):
    serializer_class = DiscussionCommentsSerializer

    def qet_queryset(self):
        user = self.kwargs['id']
        return DiscussionComments.objects.filter(user=id)

class SendReport(CreateAPIView):
    serializer_class = ReportSerializer

    def qet_queryset(self):
        user = self.kwargs['id']
        return DiscussionReport.objects.filter(user=id)




