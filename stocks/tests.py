from django.test import TestCase
from django.contrib.auth import get_user_model
from stocks.models import Stock
from rest_framework.request import Request
from rest_framework.test import APIRequestFactory
from stocks.serializers import StockSerializer


class OrderSerializerTest(TestCase):
    def setUp(self):
        self.stock = Stock.objects.create(
            symbol='GLO',
            name='Globe Telecom Inc',
            price=150.00
        )

    def test_order_serializer(self):
        serializer = StockSerializer(instance=self.stock)
        data = serializer.data
        self.assertEqual(data['symbol'], 'GLO')
        self.assertEqual(data['name'], 'Globe Telecom Inc')
        self.assertEqual(data['price'], '150.00')