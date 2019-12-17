from rest_framework import serializers
from .models import Discussion, DiscussionComments, DiscussionReport
from languages.serializers import LanguageSerializer

class DiscussionSerializer(serializers.ModelSerializer):
    language = LanguageSerializer()
    #author = UserSerializer()
    class Meta:
        model = Discussion
        fields = (
            'title',
            'detail',
            'language',
            'author',
            'date'
        )

class DiscussionCommentsSerializer(serializers.ModelSerializer):
    #user = UserSerializer()
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
    #author = UserSerializer()
    class Meta:
        model = DiscussionReport
        fields = (
            'text',
            'author',
            'discussion',
        )

class ViewsSerializer(serializers.ModelSerializer):
    discussion = DiscussionSerializer()
     class Meta:
        model = DiscussionReport
        fields = (
            'discussion',
            'amount',
        )