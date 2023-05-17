from django.core.management.base import BaseCommand
from src.settings import BASE_DIR
from snifa.models import Snifa
import json


class Command(BaseCommand):
    help = 'Read scraper.json file and store the information in snifa model'

    def read_json_file(self) -> list:
        """
           read json file that contain the information of web scraping

           :return: list with dict object
        """
        filename = BASE_DIR / "scraper.json"
        with open(filename, "r") as openfile:
            json_object = json.load(openfile)
        return json_object

    def store_data(self) -> None:
        """
            method that store in snifa model the information obtained for web scrapping process

            :return: None
        """
        print("Read json file")
        snifa_objects = self.read_json_file()
        print("Store in snifa model")
        for snifa_object in snifa_objects:
            Snifa.objects.create(
                file=snifa_object.get('file'),
                auditable_unit=snifa_object.get('auditable_unit'),
                auditable_unit_url=snifa_object.get('auditable_unit_url'),
                company_name=snifa_object.get('company_name'),
                category=snifa_object.get('category'),
                region=snifa_object.get('region'),
                state=snifa_object.get('state'),
                detail_url=snifa_object.get('detail_url'),
            )
        return None

    def handle(self, *args, **kwargs):
        print("init process")
        self.store_data()
        print("store has finished")
