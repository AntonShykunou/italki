from django.db import models
from django.db.models import Model
from users.models import User
from languages.models import Language
from datetime import datetime
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Discussion(models.Model):
    title = models.TextField(blank=False)
    detail = models.TextField(blank=False)
    language = models.ForeignKey(
        Language, on_delete=models.SET_NULL, null=True, related_name='discussions')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='discussions')
    date = models.DateTimeField(auto_now_add=True)


class DiscussionComment(models.Model):
    text = models.TextField(blank=False)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='discussioncomments')
    discussion = models.ForeignKey(
        Discussion, on_delete=models.CASCADE, related_name='discussioncomments')


class DiscussionReport(models.Model):
    discussion = models.ForeignKey(
        Discussion, on_delete=models.SET_NULL, null=True, related_name='discussionreport')
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name='discussionreport')
    text = models.TextField(blank=False)


