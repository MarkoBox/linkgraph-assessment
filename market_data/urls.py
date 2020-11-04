from django.urls import path
from . import views
from .api.views import LatestTradeDataView

urlpatterns = [
    path('', views.index, name='index_view'),
    path('api/trade-data', LatestTradeDataView.as_view(), name='trade_data')
]
