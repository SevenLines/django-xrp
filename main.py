import pprint

from exmo import ExmoAPI

API_KEY = 'K-6fc4f4c01e71d65fec9c30054932a4c6f7080e53'
# обратите внимание, что добавлена 'b' перед строкой
API_SECRET = 'S-900f3c448709995c59b279b76cb959d9d0f728a9'

# Тонкая настройка
CURRENCY_1 = 'BTC'
CURRENCY_2 = 'USD'

CURRENCY_1_MIN_QUANTITY = 0.001  # минимальная сумма ставки - берется из https://api.exmo.com/v1/pair_settings/

# базовые настройки
API_URL = 'api.exmo.com'
API_VERSION = 'v1'


# Свой класс исключений
class ScriptError(Exception):
    pass


class ScriptQuitCondition(Exception):
    pass


CURRENT_PAIR = CURRENCY_1 + '_' + CURRENCY_2


# Example
exmo = ExmoAPI()
# print(exmo.user_info())
pprint.pprint(exmo.ticker('BTC_USD'))


