from django.contrib.contenttypes.fields import GenericRelation
from likes.models import Like
from django.db import models
from users.models import Teacher
from hitcount.models import HitCountMixin, HitCount

class Article(models.Model):
    title = models.CharField(max_length=50, db_index=True)
    body = models.TextField(db_index=True)
    date_pub = models.DateTimeField(auto_now_add=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    likes = GenericRelation(Like)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk', related_query_name='hit_count_generic_relation')
    
    
    def __str__(self):
        return self.title

    @property
    def total_likes(self):
        return self.likes.count()
