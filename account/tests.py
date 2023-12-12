from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from orders.models import Order 
from stocks.models import Stock


class AccountDetailAPIViewTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword',
            first_name='First',
            last_name='LastName',
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_account_detail_api_view(self):
        response = self.client.get('/api/account/user/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        results = response.data

        self.assertEqual(results['last_name'], self.user.last_name)
        self.assertEqual(results['first_name'], self.user.first_name)


class OrderAccountListAPIViewTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword',
            first_name='First',
            last_name='LastName',
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        self.stock_1 = Stock.objects.create(symbol='BDO', name='BDO Unibank Inc', price=150.00)
        self.stock_2 = Stock.objects.create(symbol='AC', name='Ayala Corp', price=648.00)
        self.order_1 = Order.objects.create(
            stock=self.stock_1,
            quantity=1,
            account=self.user
        )
        self.order_2 = Order.objects.create(
            stock=self.stock_2,
            quantity=1,
            account=self.user
        )

    def test_order_account_list_api_view(self):
        response = self.client.get('/api/account/orders/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        results = response.data
        
        self.assertEqual(len(results), 2)
        self.assertEqual(results[1]['order_code'], 'ORD-00002')
        self.assertEqual(results[0]['order_code'], 'ORD-00001')

