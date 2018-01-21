from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import list_route
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from main.exmo_api import ExmoAPI
from django.conf import settings

from main.models import Ticker


class ExmoViewSet(GenericViewSet):
    @list_route
    def ticker(self):
        api = ExmoAPI()
        data = api.ticker(settings.CURRENCY)
        model = Ticker.objects.create(**data)
        print(data)
        return Response(data)