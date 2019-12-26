from rest_framework import serializers
from .models import Language, LearningLanguage, NativeLanguage
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

class NativeLanguageSerializer(serializers.ModelSerializer):
    language = LanguageSerializer()
    user = UserSerializer()
    
    class Meta:
        model = NativeLanguage
        field = (
            'language',
            'user'
        )