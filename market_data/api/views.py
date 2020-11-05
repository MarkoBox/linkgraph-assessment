from rest_framework.pagination import PageNumberPagination
from rest_framework import generics
from .serializers import TradeDataSerializer, CoinSerializer
from ..models import TradeData, Coin


class TopPaginator(PageNumberPagination):
    page_size = 20
    page_query_param = 'page_size'
    max_page_size = 20


class LatestTradeDataView(generics.ListAPIView):
    serializer_class = TradeDataSerializer
    pagination_class = TopPaginator

    def get_queryset(self):
        latest_update_time = TradeData.objects.latest('update_time').update_time
        return TradeData.objects.filter(update_time__exact=latest_update_time)\
            .exclude(weighted_price__isnull=True)\
            .order_by('-weighted_price')


class CoinView(generics.ListAPIView):
    serializer_class = CoinSerializer

    def get_queryset(self):
        return Coin.objects.all()
