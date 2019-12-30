from rest_framework import serializers
from .models import Discussion, DiscussionComments, DiscussionReport
from languages.serializers import LanguageSerializer
from users.serializers import UserSerializer

class DiscussionSerializer(serializers.ModelSerializer):
    language = LanguageSerializer()
    user = UserSerializer()
    class Meta:
        model = Discussion
        fields = (
            'title',
            'detail',
            'language',
            'user',
            'date'
        )

class DiscussionCommentsSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    discussion = DiscussionSerializer()
    class Meta:
        model = DiscussionComments
        fields = (
            'text',
            'user',
            'discussion'
        )

class ReportSerializer(serializers.ModelSerializer):
    discussion = DiscussionSerializer()
    user = UserSerializer()
    class Meta:
        model = DiscussionReport
        fields = (
            'text',
            'user',
            'discussion',
        )