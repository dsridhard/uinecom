# from rest_framework.generics import ListAPIView
# from .models import Customer
# from .serializers import CustomerSerializer
# # Create your views here.
# class CustomerListAPIView(ListAPIView):
#     queryset=Customer.objects.all()
#     serializer_class=CustomerSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Customer,Address,CustomerProfile  # Replace with your actual model
from .serializers import CustomerSerializer,AddressSerializer,CustomerProfileSerializer  # Create this if not done yet
class CustomerListAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AddressListAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        address=Address.objects.all()
        serializer =AddressSerializer(address,many=True)
        return Response(serializer.data)
    permission_classes = [IsAuthenticated]
    def post(self,request):
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages,status=status.HTTP_400_BAD_REQUEST)

class CustomerProfileListAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        profiles=CustomerProfile.objects.all()
        serializer = CustomerProfileSerializer(profiles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = CustomerProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # other methods here...
    # def put(self, request, pk):
    #     customer = Customer.objects.get(pk=pk)
    #     serializer = CustomerSerializer(customer, data=request.data)  
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # def delete(self, request, pk):
    #     customer = Customer.objects.get(pk=pk)
    #     customer.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
    # other methods here...
    # def patch(self, request, pk):
    #     customer = Customer.objects.get(pk=pk)
    #     serializer = CustomerSerializer(customer, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # other methods here...
    