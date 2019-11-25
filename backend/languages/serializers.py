from rest_framework import serializers
from .models import Language, LearningLanguage

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = (
            'title',
            'photo',
        )


class LearningLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = LearningLanguage
        fields = (
            'language',
            'skills',
        )