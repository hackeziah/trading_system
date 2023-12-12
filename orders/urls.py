from django.urls import path

from orders.views import OrderListAPIView, OrderCreateAPIView

urlpatterns = [
    path('api/orders/', OrderListAPIView.as_view(), name='orders'),
    path('api/create/order/', OrderCreateAPIView.as_view(), name='order-create'),
]