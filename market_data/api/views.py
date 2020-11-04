from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .serializers import TradeDataSerializer, CoinSerializer
from ..models import TradeData, Coin


class LatestTradeDataView(generics.ListAPIView):
    serializer_class = TradeDataSerializer

    def get_queryset(self):
        latest_update_time = TradeData.objects.latest('update_time').update_time
        return TradeData.objects.filter(update_time__exact=latest_update_time)


class CoinView(generics.ListAPIView):
    serializer_class = CoinSerializer

    def get_queryset(self):
        return Coin.objects.all()
