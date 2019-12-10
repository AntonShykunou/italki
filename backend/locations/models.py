from django.db import models
from .choices import COUNTRIES_CHOISE

class Country(models.Model):
    name = models.CharField(max_length=100, choices=COUNTRIES_CHOISE)

    def __str__(self):
        return self.name
    
    class Meta:
        varbose_name_plural = 'Contries'


class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='cities')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return "{0}, {1}".format(self.name, self.country.name)
    
    class Meta:
        varbose_name_plural = 'Cities'