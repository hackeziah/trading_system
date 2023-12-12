from django.urls import path

from account.views import OrderAccountListAPIView, AccountDetailAPIView

urlpatterns = [
    path('api/account/user/', AccountDetailAPIView.as_view(), name='account-details'),
    path('api/account/orders/', OrderAccountListAPIView.as_view(), name='account-orders'),
]