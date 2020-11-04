from rest_framework import serializers

from ..models import TradeData, Coin


class TradeDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = TradeData
        fields = ['currency_volume', 'weighted_price', 'update_time']


class CoinSerializer(serializers.ModelSerializer):
    trade_data = TradeDataSerializer(many=True)

    class Meta:
        model = Coin
        fields = ['ticker_symbol', 'trade_data']
