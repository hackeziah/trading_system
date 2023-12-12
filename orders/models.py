from account.models import Account
from stocks.models import Stock

from base.models import BaseModel

from django.db import models


class Order(BaseModel):
    BUY = 'buy'
    SELL = 'sell'

    ORDER_TYPE_CHOICES = [
        (True, 'Buy'),
        (False, 'Sell'),
    ]
    order_code = models.CharField(max_length=255)
    account = models.ForeignKey('account.Account', on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    order_type = models.BooleanField(choices=ORDER_TYPE_CHOICES, default=True)
    quantity = models.PositiveIntegerField()
    total_amount = models.DecimalField(max_digits=12, decimal_places=2)

    def _generate_order_code(self):
        if not self.order_code:
            last_order = Order.objects.order_by('-id').first()
            base_code = 'ORD' 
            if last_order:
                order_number = last_order.id + 1
            else:
                order_number = 1
        self.order_code = f"{base_code}-{order_number:05d}"

    def save(self, *args, **kwargs):
        self._generate_order_code()
        self.total_amount = self.stock.price * self.quantity 
        super().save(*args, **kwargs)
        
    def __str__(self):
        order_type = "Buy" if self.order_type else "Sell"
        return f"{order_type} {self.quantity} {self.stock.symbol} shares"