from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from market_data.models import Coin, TradeData
from market_data.api.serializers import TradeDataSerializer
from django.utils import timezone

client = Client()


class GetLatestTradeData(TestCase):
    """ Test module for GET latest trade data API """

    def setUp(self):
        c = Coin.objects.create(
            ticker_symbol='btcdeEUR')
        TradeData.objects.create(currency_volume=0, weighted_price=None, update_time=timezone.now(), coin=c)

    def test_get_latest_data(self):
        response = client.get(reverse('trade_data'))
        trade_data = TradeData.objects.all()
        serializer = TradeDataSerializer(trade_data, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
