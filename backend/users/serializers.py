from .models import User, CommunicationTool, Teacher
from languages.serializers import LanguageSerializer, LearningLanguageSerializer
from rest_framework import serializers


class CommunicationToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunicationTool
        fields = (
            'name',
            'address' 
        )


class UserSerializer(serializers.ModelSerializer):
    communication_tool = CommunicationToolSerializer(many=True, read_only=True)
    native_languages = LanguageSerializer(many=True)
    learning_languages = LearningLanguageSerializer(many=True)
   
    class Meta:
        model = User
        fields = (
            'email', 
            'username', 
            'birthday',
            'gender',
            'time_zone',
            'photo',
            'communication_tool', 
            'introduction',
            'native_languages', 
            'learning_languages', 
            'last_visit'
        )

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'email', 
            'username', 
            'birthday',
            'gender',
            'time_zone',
            'photo',
            'communication_tool', 
            'introduction',
            'native_languages', 
            'learning_languages', 
            'last_visit'
        )
    

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'email', 
            'username', 
            'birthday',
            'password'
        )
        
        extra_kwargs = {
            'password': {'write_only': True}
        }

   
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
class TeacherSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Teacher
        fields = (
            'user', 'video',
        )