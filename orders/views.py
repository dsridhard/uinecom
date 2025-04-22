from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Order, OrderItem ,ShippingAddress  # Replace with your actual model
from .serializers import OrderSerializer, OrderItemSerializer ,ShippingAddressSerializer # Create this if not done yet

class OrderListAPIView(APIView):
    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderItemListAPIView(APIView):
    def get(self, request, order_id):
        order = Order.objects.get(id=order_id)
        order_items = OrderItem.objects.filter(order=order)
        serializer = OrderItemSerializer(order_items, many=True)
        return Response(serializer.data)
    def post(self, request, order_id):
        order = Order.objects.get(id=order_id)
        serializer = OrderItemSerializer(data=request.data, context={'order': order})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
# Create your views here.

class ShippingAddressListAPIView(APIView):
    def get(self, request, order_id):
        order = Order.objects.get(id=order_id)
        shipping_addresses = ShippingAddress.objects.filter(order=order)
        serializer = ShippingAddressSerializer(shipping_addresses, many=True)
        return Response(serializer.data)
    def post(self, request, order_id):
        order = Order.objects.get(id=order_id)
        serializer = ShippingAddressSerializer(data=request.data, context={'order': order})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)