from rest_framework import serializers
from .models import Language, LearningLanguage
from users.serializers import UserSerializer

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = (
            'title',
            'photo',
        )


class LearningLanguageSerializer(serializers.ModelSerializer):
    language = LanguageSerializer()
    
    class Meta:
        model = LearningLanguage
        fields = (
            'language',
            'skills',
        )
