from rest_framework import serializers
from checkout.models import Product, Discount, CartItem

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class DiscountSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = Discount
        fields = "__all__"

class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = CartItem
        fields = "__all__"

class CheckoutSerializer(serializers.Serializer):
    items = serializers.CharField()