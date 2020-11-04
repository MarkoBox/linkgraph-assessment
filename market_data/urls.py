from django.urls import path
from . import views
from .api.views import LatestTradeDataView, CoinView

urlpatterns = [
    path('', views.index, name='index_view'),
    path('api/trade-data', LatestTradeDataView.as_view(), name='trade_data'),
    path('api/coin', CoinView.as_view(), name='coin')
]
