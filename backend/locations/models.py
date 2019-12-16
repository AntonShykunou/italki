from django.db import models
from users.models import User
# from .choices import COUNTRIES_CHOISE

class Country(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, related_name='cities')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return "{0}, {1}".format(self.name, self.country.name)
    