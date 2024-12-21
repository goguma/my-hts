from django.contrib import admin

# Register your models here.
from .models import Account, Stock, Transaction, Profit, Dividend

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('account_name', 'balance', 'creation_date')
    search_fields = ('account_name',)

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('stock_symbol', 'stock_name')
    search_fields = ('stock_symbol', 'stock_name')

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('account', 'stock', 'transaction_date', 'transaction_type', 'quantity', 'price')
    search_fields = ('account__account_name', 'stock__stock_name')
    list_filter = ('transaction_type',)

@admin.register(Profit)
class ProfitAdmin(admin.ModelAdmin):
    list_display = ('account', 'stock', 'total_invested', 'total_return', 'profit_date')
    search_fields = ('account__account_name', 'stock__stock_name')

@admin.register(Dividend)
class DividendAdmin(admin.ModelAdmin):
    list_display = ('account', 'stock', 'dividend_amount', 'dividend_date')
    search_fields = ('account__account_name', 'stock__stock_name')

