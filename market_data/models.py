from django.db import models
from .managers import ApiCallHistoryManager, CoinManager, TradeDataManager


class ApiCallHistory(models.Model):
    returned_json = models.JSONField()
    update_time = models.DateTimeField()

    objects = ApiCallHistoryManager()


class Coin(models.Model):
    ticker_symbol = models.TextField(unique=True, max_length=20)

    objects = CoinManager()


class TradeData(models.Model):
    currency_volume = models.DecimalField(max_digits=25, decimal_places=2, null=True, blank=True,
                                          verbose_name='Currency volume') # TODO: 4 places for consistency
    weighted_price = models.DecimalField(max_digits=25, decimal_places=4, null=True, blank=True,
                                         verbose_name='Weighted Price')
    update_time = models.DateTimeField()
    coin = models.ForeignKey(Coin, on_delete=models.CASCADE, null=True, blank=True, related_name='trade_data')

    objects = TradeDataManager()

