from rest_framework import serializers
from .models import Lesson, LessonSession
from users.serializers import UserSerializer
from users.models import User
from .choices import CHOICES_STATUS

class LessonSerializer(serializers.ModelSerializer):
    # teacher = TeacherSerializer(read_only=True)
    
    class Meta:
        model = Lesson
        fields = (
            'teacher',
            'title',
            'price',
            'description'
        )
        

class LessonSessionSerializer(serializers.ModelSerializer):
    student = UserSerializer()
    lesson = LessonSerializer()

    class Meta:
        model = LessonSession
        fields = (
            'lesson',
            'student',
            'status',
        )
