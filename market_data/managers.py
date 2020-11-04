from django.db.models import QuerySet, Manager
import requests
from django.utils import timezone
from django.db import connection


class ApiCallHistoryQuerySet(QuerySet):
    pass


class ApiCallHistoryManager(Manager):
    def get_queryset(self):
        return ApiCallHistoryQuerySet(self.model, using=self._db)

    def import_new_market_data(self):
        url = "http://api.bitcoincharts.com/v1/markets.json"
        update_time = timezone.now()

        data = requests.get(url=url).json()
        objs = [self.model(returned_json=line, update_time=update_time) for line in data]
        self.model.objects.bulk_create(objs)
        print(update_time)
        return self.model.objects.filter(update_time=update_time), update_time


class CoinQuerySet(QuerySet):
    pass


class CoinManager(Manager):
    def get_queryset(self):
        return ApiCallHistoryQuerySet(self.model, using=self._db)

    def update_new_coins(self):
        with connection.cursor() as cursor:
            cursor.execute("""INSERT INTO market_data_coin(ticker_symbol)
        SELECT DISTINCT returned_json ->> 'symbol' from market_data_apicallhistory
        LEFT JOIN market_data_coin
            ON  returned_json ->> 'symbol' = market_data_coin.ticker_symbol
        WHERE market_data_coin.ticker_symbol IS NULL;""")
        return None


class TradeDataQuerySet(QuerySet):
    pass


class TradeDataManager(Manager):
    def get_queryset(self):
        return TradeDataQuerySet(self.model, using=self._db)

    def import_data_updated_at(self, update_time):
        with connection.cursor() as cursor:
            cursor.execute("""WITH new_data AS (
        SELECT returned_json, update_time, market_data_coin.id AS coin_id
        FROM market_data_apicallhistory
                LEFT JOIN market_data_coin
                        ON market_data_apicallhistory.returned_json ->> 'symbol' = market_data_coin.ticker_symbol
        WHERE update_time = %s
        )
        INSERT
            INTO market_data_tradedata (currency_volume, weighted_price, update_time, coin_id)
            SELECT CAST(new_data.returned_json ->> 'currency_volume' AS DECIMAL),
                   CAST(new_data.returned_json ->> 'weighted_price' AS DECIMAL),
                   new_data.update_time,
                   new_data.coin_id FROM new_data;""", params=[update_time])
        return None
