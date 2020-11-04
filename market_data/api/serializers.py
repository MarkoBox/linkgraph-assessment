from rest_framework import serializers

from ..models import TradeData, Coin


class CoinSerializer(serializers.ModelSerializer):

    class Meta:
        model = Coin
        fields = ['ticker_symbol']


class TradeDataSerializer(serializers.ModelSerializer):
    coin = CoinSerializer()

    class Meta:
        model = TradeData
        fields = ['currency_volume', 'weighted_price', 'update_time', 'coin']
