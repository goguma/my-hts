# from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Account, Stock, Transaction, Profit, Dividend
from .serializers import AccountSerializer, StockSerializer, TransactionSerializer, ProfitSerializer, DividendSerializer

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class ProfitViewSet(viewsets.ModelViewSet):
    queryset = Profit.objects.all()
    serializer_class = ProfitSerializer

class DividendViewSet(viewsets.ModelViewSet):
    queryset = Dividend.objects.all()
    serializer_class = DividendSerializer
