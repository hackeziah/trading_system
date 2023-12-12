from rest_framework import serializers
from django.db.models import Sum

from account.models import Account

class AccountSerializer(serializers.ModelSerializer):
    
    total_invested = serializers.SerializerMethodField('get_invested')
    sell = serializers.SerializerMethodField('get_sell')


    def get_invested(self, obj: Account):
        item = obj.order_set.filter(order_type=1).aggregate(final_amount=Sum('total_amount'))
        return str("{:.2f}".format(item['final_amount'])) if item['final_amount'] else "0.00"

    def get_sell(self, obj: Account):
        item = obj.order_set.filter(order_type=0).aggregate(final_amount=Sum('total_amount'))
        return str("{:.2f}".format(item['final_amount'])) if item['final_amount'] else "0.00"
    
    
    class Meta: 
        model = Account
        fields = (
                'first_name',
                'last_name',
                'address',
                'phone_number',
                'balance',
                'total_invested',
                'sell',
            )


class AccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Account
        fields = ['url', 'username', 'email', 'is_staff']
