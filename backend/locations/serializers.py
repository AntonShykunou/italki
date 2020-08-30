from rest_framework import serializers
from .models import City, Country


class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = (
            'id',
            'name',
        )


class CitySerializer(serializers.ModelSerializer):
    country = CountrySerializer()
    class Meta:
        model = City
        fields = (
            'id',
            'name',
            'country'
        )