from django.core.management.base import BaseCommand, CommandError
from ._private import unzip_file, get_cities_and_countries, get_countries, save_cities_list, save_countries_list
import requests, os


URL_CITIES = 'http://download.geonames.org/export/dump/cities15000.zip'
TEMP_PATH_FILE = 'cities15000.txt'

class Command(BaseCommand):
    help = 'Load cities in db'

    def handle(self, *args, **options):
        unzip_file(URL_CITIES )
        save_countries_list(get_countries(TEMP_PATH_FILE))
        save_cities_list(get_cities_and_countries(TEMP_PATH_FILE)) 
        os.remove(TEMP_PATH_FILE)