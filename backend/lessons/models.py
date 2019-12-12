from django.db import models
from users.models import User, Teacher
from .choices import CHOICES_STATUS
from datetime import datetime

class Lesson(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True, related_name='lessons')
    title = models.CharField(max_length=30,  blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    date = models.DateField(default=datetime.now, blank=True)
    description = models.CharField(max_length=20, blank=True)
    
    def Meta():
        verbose_name = 'Lesson'
        verbose_name_plural = 'Lessons'

    def __str__(self):
        return self.title


class LessonSession(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='lessonsessions')
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lessonsessions')
    status = models.CharField(max_length=1, choices=CHOICES_STATUS, default=0)

    def __str__(self):
        return '{0}_session'.format(self.lesson.title)

    def Meta():
        verbose_name = 'LessonSession'
        verbose_name_plural = 'LessonSessions'
