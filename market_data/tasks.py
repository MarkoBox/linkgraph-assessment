from market_data.models import ApiCallHistory, Coin, TradeData
from celery import shared_task


def update_market_data():
    update_time = ApiCallHistory.objects.import_new_market_data()[1]
    Coin.objects.update_new_coins()
    TradeData.objects.import_data_updated_at(update_time=update_time)


@shared_task
def hello():
    print("Hello there!")
