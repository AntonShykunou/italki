from django.db import models

class Country(models.Model):
    # source_id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta():
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'

class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='cities')
       
    def __str__(self):
        return "{0}, {1}".format(self.name, self.country.name)
    
    class Meta():
        verbose_name = 'City'
        verbose_name_plural = 'Cities'
    