from django.db import models
import datetime
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.mail import send_mail
from .validations import validate_birthday
from locations.models import Country, City
from lessons.models import Lesson
from languages.models import Language, LearningLanguage
import pytz


def get_user_photo_path(instance, filename):
    return "photos/{0}/{1}".format(instance.username, filename)


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(
            self, email, username, birthday,
            password, **extra_fields):

        if not email:
            raise ValueError("The given email must be set")
        if not username:
            raise ValueError("The given username must be set")
        if not birthday:
            raise ValueError("The given birthday must be set")

        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(
            email=email,
            username=username,
            birthday=birthday,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, username,  birthday,
                    password=None, **extra_fields):

        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("is_teacher", False)
        return self._create_user(
            email, username, birthday, password, **extra_fields
        )

    def create_superuser(self, email, username, birthday, password,
                        **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_teacher", True)
        if not  extra_fields.get("is_teacher"):
            raise ValueError("Superuser must have is_teacher=True.")
        if not extra_fields.get("is_staff"):
            raise ValueError("Superuser must have is_staff=True.")
        if not extra_fields.get("is_superuser"):
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(
            email, username, birthday, password,
            **extra_fields
        )


class CommunicationTool(models.Model):
    name = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=20, blank=True)


class User(AbstractBaseUser, PermissionsMixin):

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    
    email = models.EmailField(unique=True)
    
    username = models.CharField(
        db_index=True,
        max_length=50,
        unique=True,
    )

    birthday = models.DateField(
        validators=[validate_birthday],
        blank=True
    )

    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))
    time_zone = models.CharField(
        max_length=40, 
        choices=TIMEZONES, 
        default='UTC'
    )

    photo = models.ImageField(upload_to=get_user_photo_path, null=True, blank=True)
    communication_tool = models.ManyToManyField(CommunicationTool, blank=True)
    introduction = models.TextField(blank=True)
    native_languages = models.ManyToManyField(Language)
    learning_languages = models.ManyToManyField(LearningLanguage)
    is_teacher = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    objects = UserManager()
    is_staff = models.BooleanField(default=False)
    last_visit = models.DateTimeField(
        default=datetime.datetime.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "birthday",]

    def __str__(self):
        return self.username

    def get_short_name(self):
        return self.username
    
    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def get_location(self):
        pass
    

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher_profile')
    video = models.URLField(blank=True)


@receiver(post_save, sender=User)
def create_user(sender, instance, created, **kwargs):
    if created:
        if instance.is_teacher:
            Teacher.objects.create(user=instance)
