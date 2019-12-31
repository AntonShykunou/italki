from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='cities')
    
    def __str__(self):
        return "{0}, {1}".format(self.name, self.country.name)
    