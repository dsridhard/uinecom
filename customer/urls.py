from django.urls import path
from .views import CustomerListAPIView,AddressListAPIView,CustomerProfileListAPIView

urlpatterns=[
    path('api/customer',CustomerListAPIView.as_view(),name='customers'),
    path('api/address',AddressListAPIView.as_view(),name='address'),
    path('api/customer_profile',CustomerProfileListAPIView.as_view(),name='customer_profile')
]