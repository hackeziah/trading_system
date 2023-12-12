from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from account.permission import IsSuperUserUser

from account.serializers import AccountSerializer, AccountLinkSerializer
from orders.serializers import OrderSerializer
from account.models import Account


class AccountDetailAPIView(generics.RetrieveAPIView):
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated]
    
    def get_object(self):
        account: Account = self.request.user
        return account


class OrderAccountListAPIView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        account: Account = self.request.user
        return account.order_set.all()


class UserViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    permission_classes = [IsAuthenticated, IsSuperUserUser]
    serializer_class = AccountLinkSerializer