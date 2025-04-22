from django.urls import path
from .views import PaymentListAPIView,TransactionListAPIView

urlpatterns = [
    path('api/payment/', PaymentListAPIView.as_view(), name='payment-list'),
    path('api/transaction/', TransactionListAPIView.as_view(), name='transaction-list'),
]