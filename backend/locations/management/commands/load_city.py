from django.core.management.base import BaseCommand, CommandError
from locations.models import City
from zipfile import ZipFile
from urllib.request import urlopen
from tempfile import TemporaryFile
from shutil import unpack_archive
import requests, json


def unzip_file(url):
    response = requests.get(url)
    with TemporaryFile() as tfile:
        tfile.write(response.content)
        tfile.seek(0)
        with ZipFile(tfile) as zfile:
            zfile.extractall('tmp/')


def parse_txt(file):
    cities = []
    with open(file, encoding='utf-8') as f:
    # open('cities.json', 'w') as out_file:
        for line in f:
            line = line.split('	')
            cities.append(line[1])
    # return json.dumps({'cities': cities})
    return cities


def create_cities(obj, _list):
    obj.objects.bulk_create(
        [obj(name) for name in _list]
    )

class Command(BaseCommand):
    help = 'Load cities in db'

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        url = 'http://download.geonames.org/export/dump/cities15000.zip'
        temp_path = 'tmp/cities15000.txt'
        unzip_file(url)
        create_cities(City, parse_txt(temp_path))
        
        # response = requests.get('http://download.geonames.org/export/dump/cities15000.zip')

        # file = TemporaryFile()
        # file.write(response.content)
        # fzip = ZipFile(file)
        # fzip.extractall('tmp/')
        # # txt_to_json('tmp/')
        # file.close()
        # fzip.close()