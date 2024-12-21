from django.db import models

# Create your models here.

class Account(models.Model):
    account_name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=20, decimal_places=2)
    creation_date = models.DateField()

    def __str__(self):
        return self.account_name

class Stock(models.Model):
    stock_symbol = models.CharField(max_length=10)
    stock_name = models.CharField(max_length=100)

    def __str__(self):
        return self.stock_name

class Transaction(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    transaction_date = models.DateField()
    transaction_type = models.CharField(max_length=4, choices=(('BUY', '매수'), ('SELL', '매도')))
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return f'{self.account.account_name} - {self.stock.stock_name} - {self.transaction_type}'

class Profit(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    total_invested = models.DecimalField(max_digits=20, decimal_places=2)
    total_return = models.DecimalField(max_digits=20, decimal_places=2)
    profit_date = models.DateField()

    def __str__(self):
        return f'{self.account.account_name} - {self.stock.stock_name}'

class Dividend(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    dividend_amount = models.DecimalField(max_digits=20, decimal_places=2)
    dividend_date = models.DateField()

    def __str__(self):
        return f'{self.account.account_name} - {self.stock.stock_name}'

