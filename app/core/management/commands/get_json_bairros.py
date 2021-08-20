import requests as r, json

from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup as bs

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.write_json("Juazeiro do Norte", self.get_bairros('juazeiro-do-norte'))
        self.write_json("Crato", self.get_bairros('crato'))

    def write_json(self, cidade, bairro):
        with open(f"static/bairros_{cidade}.json", "w") as f:
            json.dump(bairro, f, ensure_ascii=False, indent=4)

    def get_bairros(self, cidade):
        base_url = f"https://www.guiamais.com.br/bairros/{cidade}-ce"
        response = r.get(base_url)
        html = bs(response.text, 'html.parser')
        bairros = [
            a.text.replace("\n", "") for a in html.find_all('section', {'class': 'cities'})[0].find_all('a')
        ]

        return bairros


