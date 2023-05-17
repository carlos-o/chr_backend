from django.core.management.base import BaseCommand
from src.settings import SNIFA_URL
from utils.utils import request_page, parse_html
import json


class Command(BaseCommand):
    help = 'performs the web scraping process of page https://snifa.sma.gob.cl/Sancionatorio/Resultado'

    def generate_json_file(self, data) -> bool:
        """
            generate a json file  with data obtained by the web scrapping

            :param data: json stringify
            :type data: text
            :return: True
        """
        with open("scraper.json", "w") as outfile:
            json.dump(data, outfile)
        return True

    def crawling_data(self) -> None:
        """
            method that performs the web scraping process
            :return: None
        """
        print("get information about the page")
        try:
            response = request_page(SNIFA_URL.format("/Sancionatorio/Resultado"), response_type="text")
        except Exception as e:
            print("Error in call")
            raise Exception(str(e))
        print("Parser the content html")
        soup = parse_html(response)
        table = soup.find("table", {"id": "myTable"})
        body = table.find("tbody")
        data = []
        print("get information to store")
        for row in body.find_all('tr'):
            scraper_data = {"file": None, "auditable_unit": [], "auditable_unit_url": [], "company_name": [],
                            "category": None, "region": None, "state": None, "detail_url": None}
            elements = row.find_all('td')[1:]
            auditable_unit = []
            auditable_unit_url = []
            for auditable in elements[1].select('li'):
                auditable_unit.append(auditable.get_text(strip=True))
                auditable_unit_url.append(SNIFA_URL.format(auditable.select_one('a').get('href')))
            company_name = []
            for name in elements[2].select('li'):
                if name.get_text(strip=True):
                    company_name.append(name.get_text(strip=True))
            scraper_data.update(
                {
                    "file": elements[0].get_text(strip=True),
                    "auditable_unit": auditable_unit,
                    "auditable_unit_url": auditable_unit_url,
                    "company_name": company_name,
                    "category": None if len(elements[3].get_text(strip=True)) == 0 else elements[3].get_text(strip=True),
                    "region": None if len(elements[4].get_text(strip=True)) == 0 else elements[4].get_text(strip=True),
                    "state": None if len(elements[5].get_text(strip=True)) == 0 else elements[5].get_text(strip=True),
                    "detail_url": None if elements[6].select_one('a').get('href') is None else
                    SNIFA_URL.format(elements[6].select_one('a').get('href'))
                }
            )
            data.append(scraper_data)
        print("Generate json file")
        self.generate_json_file(data)
        return None

    def handle(self, *args, **kwargs):
        print("init process")
        self.crawling_data()
        print("scraping has finished")
