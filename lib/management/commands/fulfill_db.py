from django.core.management.base import BaseCommand, CommandError
from lib.models import *
import requests
from bs4 import BeautifulSoup as bs


class Command(BaseCommand):
    help = 'Fulfill Database'

    def handle(self, *args, **options):
        url = 'https://gtmarket.ru/ratings/newsweeks-top-100-books'

        resp = requests.session().get(url)

        soup = bs(resp.content, 'html.parser')

        table = soup.select(
            '#main > article > div > table > tbody:nth-child(4) > tr.text > td > div > table > tbody')
        info = table[0].findAll('tr')

        for data in info:
            text = data.text.split('\n')[2:-2]
            author = text[0].replace('\xad', '')
            title = text[1].replace('\xad', '')
            aut, created_aut = Author.objects.get_or_create(name=author)
            b, created_b = Book.objects.get_or_create(
                title=title, author=aut)
