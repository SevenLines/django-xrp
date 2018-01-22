import traceback
from time import sleep

from django.conf import settings
from django.core.management import BaseCommand

from main.exmo_api import ExmoAPI
from main.models import Ticker


class Command(BaseCommand):
    def handle(self, *args, **options):
        api = ExmoAPI()
        while True:
            try:
                data = api.ticker(settings.CURRENCY)
            except Exception as ex:
                traceback.print_exc()
            else:
                ticker = Ticker.objects.create(**data)
                print(ticker.pk)
            sleep(1)