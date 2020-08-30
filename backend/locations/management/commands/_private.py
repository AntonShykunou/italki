from zipfile import ZipFile
from tempfile import TemporaryFile
from locations.models import City, Country
import requests, json


def unzip_file(url):
    response = requests.get(url)
    with TemporaryFile() as tfile:
        tfile.write(response.content)
        tfile.seek(0)
        with ZipFile(tfile) as zfile:
            zfile.extractall()

def get_countries(file):
    countries = []
    with open(file, encoding='utf-8') as f:
        for line in f:
            line = line.split('	')
            countries.append(line[8])
    return sorted(set(countries))

def get_cities_and_countries(file):
    cities_and_countries = {}
    with open(file, encoding='utf-8') as f:
        for line in f:
            line = line.split('	')
            if line[8] not in cities_and_countries.keys():
                cities_and_countries.update({line[8]:[]})
        f.seek(0)
        for c in f:
            c = c.split('	')
            cities_and_countries[c[8]].append(c[1])
    return cities_and_countries

def save_countries_list(list_countries):
    Country.objects.bulk_create(
        [Country(name=name) for name in list_countries]
    )

def list_objects_cities(cities_and_countries):
    countries = Country.objects.in_bulk()
    cities = []
    for id in countries:
        for k, v in cities_and_countries.items():
            for c in v:
                if countries[id].name == k:
                    cities.append(City(name=c, country_id=id))
    return cities

def save_cities_list(cities_and_countries):
    City.objects.bulk_create(
       list_objects_cities(cities_and_countries)
    )
    