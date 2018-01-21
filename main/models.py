from django.db import models

# Create your models here.


class Ticker(models.Model):
    avg = models.DecimalField(max_digits=20, decimal_places=8)
    buy_price = models.DecimalField(max_digits=20, decimal_places=8)
    high = models.DecimalField(max_digits=20, decimal_places=8)
    last_trade = models.DecimalField(max_digits=20, decimal_places=8)
    low = models.DecimalField(max_digits=20, decimal_places=8)
    sell_price = models.DecimalField(max_digits=20, decimal_places=8)
    updated = models.DecimalField(max_digits=20, decimal_places=8)
    vol = models.DecimalField(max_digits=20, decimal_places=8)
    vol_curr = models.DecimalField(max_digits=20, decimal_places=8)