from django.db import models
from users.models import User

CHOISES_STATUSE = (
    (0, 'pending'),
    (1, 'approved'),
    (2, 'declined'),
    (3, 'finished')
)


class Lesson(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='teacher')
    title = models.CharField(max_length=30)
    price = models.FloatField()
    date = models.DateField()
    description = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class LessonSession():
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='lesson')
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student')
    status = models.CharField(choices=CHOISES_STATUSE, default=0)

    def __str__(self):
        return "{0} {1}".format(student, lesson)

    # def create_lesson(sender, lesson_request):
    #     pass

    # def lesson_request_changed(sender, lesson_request):
    #     pass
    
    # def lesson_request_canceled(sender, lesson_request):
    #     pass

    # def lesson_request_declined(sender, lesson_request):
    #     pass


