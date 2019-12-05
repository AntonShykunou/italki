from django.contrib.contenttypes.fields import GenericRelation
from likes.models import Like
from django.db import models
from users.models import Teacher

class Article(models.Model):
    title = models.CharField(max_length=50, db_index=True)
    body = models.TextField(db_index=True)
    date_pub = models.DateTimeField(auto_now_add=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    likes = GenericRelation(Like)
    is_published = models.BooleanField(('Is published'), default=False)
    
    
    def __str__(self):
        return self.title


    @property
    def total_likes(self):
        return self.likes.count()
