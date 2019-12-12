from rest_framework import serializers
from .models import Lesson, LessonSession
from users.serializers import UserSerializer, TeacherSerializer
from users.models import User


class LessonSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer(read_only=True)
    
    class Meta:
        model = Lesson
        fields = (
            'teacher',
            'title',
            'price',
            'date',
            'description',
        )
        

class LessonSessionSerializer(serializers.ModelSerializer):
    student = UserSerializer()
    lesson = LessonSerializer()
    status = serializers.CharField(source='get_status_display')

    class Meta:
        model = LessonSession
        fields = (
            'lesson',
            'student',
            'status',
        )

    # def get_status(self, obj):
    #     return obj.get_status_display()