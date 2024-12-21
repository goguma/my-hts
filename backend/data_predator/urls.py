from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AccountViewSet, StockViewSet, TransactionViewSet, ProfitViewSet, DividendViewSet

router = DefaultRouter()
router.register(r'accounts', AccountViewSet)
router.register(r'stocks', StockViewSet)
router.register(r'transactions', TransactionViewSet)
router.register(r'profits', ProfitViewSet)
router.register(r'dividends', DividendViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
