from django.db import models
from django.db.models import Model
from users.models import User
from languages.models import Language
from datetime import datetime
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Discussion(models.Model):
    title = models.TextField(blank=True)
    detail = models.TextField(blank=True)
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True, related_name='discussions')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='discussions')
    date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.author

class DiscussionComments(models.Model):
    text = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='discussioncomments')
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE, related_name='discussioncomments')

class DiscussionReport(models.Model):
    discussion = models.ForeignKey(Discussion, on_delete=models.SET_NULL, null=True, related_name='discussionreport')
    author = models.ForeignKey(User, on_delete=models.SET_NULL,  null=True, related_name='discussionreport')
    text = models.TextField(blank=True)

class ViewsIndicator(models.Model):
    discussion = models.ForeignKey(Discussion, on_delete=models.SET_NULL, null=True, related_name='discussionreport')
    amount = models.IntegerField(null=True)
