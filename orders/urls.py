from django.urls import path
from .views import OrderListAPIView, OrderItemListAPIView,ShippingAddressListAPIView

urlpatterns = [
    path('api/order/', OrderListAPIView.as_view(), name='order-list'),
    path('api/order-item/', OrderItemListAPIView.as_view(), name='order-item-list'),
    path('api/shipping-address/', ShippingAddressListAPIView.as_view(), name='shipping-address-list'),
]