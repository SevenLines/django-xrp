from pprint import pprint

from django.test import TestCase

# Create your tests here.
from main.exmo_api import ExmoAPI


class ExmoApiTestCase(TestCase):
    def setUp(self):
        self.exmo = ExmoAPI()

    def test_ticker(self):
        data = self.client.get('/exmo/ticker')
        pprint(data)

