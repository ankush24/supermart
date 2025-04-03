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
        serializer = CheckoutSerializer(data=request.data)
        if serializer.is_valid():
            items = serializer.validated_data["items"]
            cart = {}

            for item in items:
                product = get_object_or_404(Product, name=item)
                if product.stock > 0:
                    cart[item] = cart.get(item, 0) + 1
                    product.stock -= 1
                    product.save()
                else:
                    return Response({"error": f"{item} is out of stock!"}, status=status.HTTP_400_BAD_REQUEST)

            total_price = 0
            breakdown = {}

            for item, quantity in cart.items():
                product = Product.objects.get(name=item)
                discount = Discount.objects.filter(product=product).first()

                if discount and quantity >= discount.min_discount_quantity:
                    discount_groups = quantity // discount.min_discount_quantity
                    remainder = quantity % discount.min_discount_quantity
                    subtotal = discount_groups * discount.discount_price + remainder * product.price
                else:
                    subtotal = quantity * product.price

                CartItem.objects.create(product=product, quantity=quantity)  # Track in cart
                total_price += subtotal
                breakdown[item] = {"quantity": quantity, "subtotal": subtotal}

            return Response({"total_price": total_price, "breakdown": breakdown})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
