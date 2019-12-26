from django.core.management.base import BaseCommand, CommandError
from locations.models import City
from zipfile import ZipFile
from itertools import groupby
import requests, json

def txt_to_json(file):
    cities = []
    with open(file, encoding='utf-8') as file:
    # open('cities.json', 'w') as out_file:
        for line in in_file:
            line = line.split('	')
            cities.append({'city': line[1]})
    return json.dumps({'cities': cities})



class Command(BaseCommand):
    help = 'Load cities in db'

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        request = requests.get('http://download.geonames.org/export/dump/cities15000.zip', stream=True)
        request.raise_for_status()
        with ZipFile('cities15000.zip', 'r') as zfile:
            cities = zfile.read('cities15000.txt')
            txt_to_json(cities)