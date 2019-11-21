from datetime import datetime
from django.db import models
from django.db.models import Model
from users.models import User, Teacher
from .validations import validate_content


class Feedback(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    recipient = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now)
    content = models.TextField(
        validators=[validate_content]
    )

    def __str__(self):
        return self.author
# Create your models here.