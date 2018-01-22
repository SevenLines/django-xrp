import sys
import http.client
import urllib.parse
import json
import hashlib
import hmac
import time
from django.conf import settings


class ApiError(Exception):
    pass


class ExmoAPI:
    def __init__(self, API_URL='api.exmo.com', API_VERSION='v1'):
        self.API_URL = API_URL
        self.API_VERSION = API_VERSION
        self.API_KEY = settings.API_KEY
        self.API_SECRET = bytes(settings.API_SECRET, encoding='utf-8')

    def sha512(self, data):
        H = hmac.new(key=self.API_SECRET, digestmod=hashlib.sha512)
        H.update(data.encode('utf-8'))
        return H.hexdigest()

    def api(self, api_method, params=None):
        if params is None:
            params = {}

        params['nonce'] = int(round(time.time() * 1000))
        params = urllib.parse.urlencode(params)

        sign = self.sha512(params)
        headers = {
            "Content-type": "application/x-www-form-urlencoded",
            "Key": self.API_KEY,
            "Sign": sign
        }
        conn = http.client.HTTPSConnection(self.API_URL)
        conn.request("POST", "/" + self.API_VERSION + "/" + api_method, params, headers)
        response = conn.getresponse().read()

        conn.close()

        try:
            obj = json.loads(response.decode('utf-8'))
            if 'error' in obj and obj['error']:
                print(obj['error'])
                raise ApiError("wrong json")
            return obj
        except json.decoder.JSONDecodeError:
            print('Error while parsing response:', response)
            raise

    def user_info(self):
        return self.api('user_info')

    def trades(self, pair='BTC_USD'):
        return self.api('trades', {
            'pair': pair
        })

    def order_book(self, pair='BTC_USD'):
        return self.api('trades', {
            'pair': pair
        })

    def ticker(self, pair=None):
        data = self.api('ticker', {
            'pair': pair
        })
        if pair:
            return data[pair]
        return data
