from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.mail import send_mail
from .validations import validate_birthday
from locations.models import Country, City
from lessons.models import Lesson
from languages.model import Language
import pytz


def get_user_photo_path(instance, filename):
    return "photos/{0}/{1}".format(instance.username, filename) #!!!!!!!


class CommunicationTool(models.Model):
    name_tool = models.CharField(max_length=20, blank=True)
    address_tool = models.CharField(max_length=20, blank=True)

class User(AbstractBaseUser, PermissionsMixin):
    teacher_profile = models.BooleanField(default=False)
    student_profile = models.BooleanField(default=False)
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.EmailField(unique=True)

    username = models.CharField(
        db_index=True,
        max_length=50,
        unique=True,
    )

    date_of_birth = models.DateField(
        validators=[validate_birthday],
        blank=True
    )

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))
    time_zone = models.CharField(
        max_length=40, 
        choices=TIMEZONES, 
        default='UTC'
    )

    photo = models.ImageField(upload_to=get_user_photo_path, null=True, blank=True)
    communication_tool = models.ManyToManyField(CommunicationTool)
    introduction = models.TextField(blank=True)
    language = models.ManyToManyField(Language) #Language is a model

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username",]


    def __str__(self):
        return self.username

    def get_short_name(self):
        return self.username
    
    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def get_location(self):
        pass

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    user.student_profile = True
    skills = models.CharField(max_length=10, blank=True)
    progress = models.IntegerField(default=0)
    #course = models.ManyToManyField(Course) #Course is a model
    TARGET_CHOICES = (
        ('Learning','Learning'),
        ('Speaking','Speaking'),
    )
    target = models.CharField(max_length=8, choices=TARGET_CHOICES)
    #community_updates = models.OneToOneField(CommunityUpdates, on_delete=models.CASCADE)

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher_profile')
    user.teacher_profile = True
    specialization = models.CharField(max_length=20, blank=True)
    skills = models.CharField(max_length=10, blank=True)
    video = models.URLField(blank=True)
    #calendar = models.OneToOneField(Calendar) # Calendar is a model
    lessons = models.ForeignKey(Lesson, on_delete = models.CASCADE) # Lesson is a model


#class CommunityUpdates(models.Model):
#    notebook_entries = 
#    questions = 
#    discussions = 
#    friends = 
#    points = 


@receiver(post_save, sender=User)
def create_user(sedner, instance, created, **kwargs):
    if created:
        if instance.student_profile:
           Student.objects.create(user=instance)
        elif instance.teacher_profile:
            Teacher.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user(sender, instance, **kwargs):
    if instance.student_profile:
        instance.student.save()
    elif instance.teacher_profile:
        instance.teacher.save()

