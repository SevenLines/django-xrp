import traceback
from json import JSONDecodeError
from time import sleep

from django.conf import settings
from django.core.management import BaseCommand

from main.exmo_api import ExmoAPI, ApiError
from main.models import Ticker


class Command(BaseCommand):
    def handle(self, *args, **options):
        api = ExmoAPI()
        while True:
            try:
                data = api.ticker(settings.CURRENCY)
            except Exception as ex:
                traceback.print_stack()
                traceback.print_exc()
            else:
                ticker = Ticker.objects.create(**data)
            sleep(1)