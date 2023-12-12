from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from account.permission import IsSuperUserUser

from account.models import Account
from orders.models import Order
from orders.serializers import OrderSerializer, OrderCreateSerializer

class OrderListAPIView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, IsSuperUserUser]
    queryset = Order.objects.all()


class OrderCreateAPIView(generics.CreateAPIView):
    serializer_class = OrderCreateSerializer
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()
