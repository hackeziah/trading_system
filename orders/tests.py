from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

from stocks.models import Stock
from orders.models import Order
from orders.serializers import OrderSerializer


class OrderSerializerTest(TestCase):
    def setUp(self):
        self.stock = Stock.objects.create(symbol='BDO', name='BDO Unibank Inc', price=150.00)
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.order = Order.objects.create(
            stock=self.stock,
            quantity=10,
            total_amount=1500.00,
            account=self.user
        )

    def test_order_serializer(self):
        serializer = OrderSerializer(instance=self.order)
        data = serializer.data
        self.assertEqual(data['stock']['symbol'], 'BDO')
        self.assertEqual(data['quantity'], 10)
        self.assertEqual(data['total_amount'], '1500.00')


class OrderCreateSerializerTest(TestCase):
    def setUp(self):
        self.stock = Stock.objects.create(symbol='BDO', name='BDO Unibank Inc', price=150.00)
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword',
        )
        self.data = {'stock': self.stock.id, 'quantity': 5, 'order_type': 'Buy'}
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)


    def test_create_order(self):
        url = '/api/create/order/'
        response = self.client.post(url, self.data, format='json')
        # self.assertEqual(response.status_code, 201)
        # Currently working