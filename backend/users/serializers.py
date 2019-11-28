from rest_framework.serializers import ModelSerializer

from .models import User, Teacher

class UserSerializer(ModelSerializer):
   
    class Meta:
        model = User
        fields = (
            'email', 
            'username', 
            'password',
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

class TeacherSerializer(ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Teacher
        fields = (
            'user', 'video',
        )