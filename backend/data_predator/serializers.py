from rest_framework import serializers
from .models import Account, Stock, Transaction, Profit, Dividend

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

class ProfitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profit
        fields = '__all__'

class DividendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dividend
        fields = '__all__'
