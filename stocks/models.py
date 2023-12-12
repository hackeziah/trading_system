from django.db import models
from base.models import BaseModel

class Stock(BaseModel):
    symbol = models.CharField(max_length=5)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f'{self.symbol} - {self.price}'
 