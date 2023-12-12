from rest_framework import serializers
from stocks.serializers import StockSerializer

from account.models import Account
from orders.models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Order
        fields = (
                'order_code',
                'stock',
                'quantity',
                'total_amount',
            )
        
    stock = StockSerializer()



class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Order
        fields = (
                'stock',
                'quantity',
                'order_type',
            )
    
    def __init__(self, *args, **kwargs):
        context = kwargs.get('context', {})
        self.request = context.get('request', None)
        super().__init__(*args, **kwargs)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['stock'] = {
            'symbol': instance.stock.symbol,
            'name': instance.stock.name,
            'price': f'{instance.stock.price}'
        }
        representation['order_type'] = "Buy" if instance.order_type else "Sell"
        representation['total_amount'] = f'{instance.total_amount}'
        representation['created_at'] = f'{instance.created_at}'
        return representation
    
    def create(self,validated_data):
        ModelClass = self.Meta.model
        account: Account =  self.request.user
        quantity = validated_data.get('quantity', None)
        stock = validated_data.get('stock', None)
        order_type = validated_data.get('order_type', 0)
        list_stocks = account.order_set.all().values("stock_id")
        stock_ids_set = {item['stock_id'] for item in list_stocks}
        balance = account.balance
        stock_price = stock.price if stock.price else 0
        total_amount = quantity * stock_price

        if (
            (order_type == 0) and 
            (not stock.id in stock_ids_set)
        ):
            raise serializers.ValidationError("You can't sell stocks that you don't have.")
        
        if (
            (order_type == 1) and (balance < total_amount)
        ):
            raise serializers.ValidationError("Insufficient Balance.")

        instance = ModelClass.objects.create(
            account=account,
            stock=stock,
            order_type=order_type,
            quantity=quantity,
        )
        if order_type == 1:
            account.balance -= total_amount
        else:
            account.balance += total_amount
        account.save()
        return instance