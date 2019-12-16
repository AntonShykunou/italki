from django.db import models
from .choices_languages import CHOICES_SKILLS, CHOISES_LANGUAGES
from users.models import User


def get_language_photo_path(instance, filename):
    return "media/languages/{0}".format(filename)


class Language(models.Model):
    title = models.CharField(max_length=30, choices=CHOISES_LANGUAGES, blank=True)
    photo = models.ImageField(upload_to=get_language_photo_path, null=True, blank=True)

    def __str__(self):
        return self.title


class LearningLanguage(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE, null=True)
    skills = models.CharField(max_length=20, choices=CHOICES_SKILLS, blank=True)

    def __str__(self):
        return "{0} {1}".format(self.language, self.skills)


class NativeLanguage(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)    