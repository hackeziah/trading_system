from base.models import BaseModel
from stocks.models import Stock

from django.contrib.auth.models import  AbstractUser, UserManager as OldUserManager
from django.db import models


class UserManager(OldUserManager):
    pass


class Account(AbstractUser, BaseModel):
    first_name = models.CharField(max_length=32, verbose_name='First Name')
    last_name = models.CharField(max_length=32, verbose_name='Last Name')
    address = models.TextField(max_length=512, blank=True)
    phone_number = models.CharField(max_length=32, verbose_name='Phone Number')
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=10000.00)


    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'

    objects = UserManager()

    def get_full_name(self):
        return f"{self.last_name}, {self.first_name}"
    
    def get_username(self):
        return f"{self.email}"

    def __str__(self):
        return self.get_full_name()

    def save(self, *args, **kwargs):
        self.first_name = self.first_name.upper()
        self.last_name = self.last_name.upper()
        super(Account, self).save(*args, **kwargs)


class Portfolio(BaseModel):
    account = models.OneToOneField(Account, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=10000.00)

    class Meta:
        verbose_name = 'Portfolio'
        verbose_name_plural = 'Portfolios'

    def __str__(self):
        return f"{self.account.username}'s Portfolio"

