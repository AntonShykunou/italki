from django.db import models
from users.models import User, Teacher
from .choices import CHOICES_STATUS, PENDING_STATUS
from datetime import datetime


class Lesson(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    description = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.title


class LessonSession(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='lessonsessions')
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lessonsessions')
    status = models.CharField(max_length=10, choices=CHOICES_STATUS, default=PENDING_STATUS)

    def __str__(self):
        return '{0}_session'.format(self.lesson.title)
