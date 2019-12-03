from rest_framework import serializers
from .models import Lesson, LessonSession
from users.serializers import UserSerializer, TeacherSerializer


class LessonSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer(many=True, required=True)
    class Meta:
        model = Lesson
        fields = (
            'teacher',
            'title',
            'price',
            'date',
            'decription'
        )
    
    # def create(self, validate_data):
    #     pass

class LessonSessionSerializer(serializers.ModelSerializer):
    student = UserSerializer(many=True, required=True)
    lesson = LessonSerializer(many=True, required=True)
    class Meta:
        model = LessonSession
        fields = (
            'lesson',
            'student',
            'status'
        )


