from django.db import models

class Lesson(models.Model):
    teacher = models.ForeignKey(teacher, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    price = models.FloatField()
    description = models.CharField(max_length=20)
    count_lessons = models.IntegerField()

    def __str__(self):
        return self.title

