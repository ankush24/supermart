from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from checkout.models import Product, Discount, CartItem
from checkout.serializers import ProductSerializer, DiscountSerializer, CartItemSerializer, CheckoutSerializer

class ProductListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class DiscountListView(generics.ListCreateAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer

class CartItemView(generics.ListCreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

class CheckoutView(APIView):
    def post(self, request):
        print(request.data)
        serializer = CheckoutSerializer(data=request.data)
        if serializer.is_valid():
            cart = serializer.validated_data["items"]
            total_price, breakdown = serializer.calculate_total(cart)
            return Response({"total_price": total_price, "breakdown": breakdown})
        return Response(serializer.errors, status=400)
