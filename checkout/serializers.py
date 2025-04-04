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
    
    def validate_items(self, items):
        cart = {}
        for item in items:
            cart[item] = cart.get(item, 0) + 1
            product = Product.objects.filter(name=item)
            if not product:
                raise serializers.ValidationError(f"Invalid product: {item}")
            print(cart)
            if not product.filter(stock__gte=cart[item]):
                raise serializers.ValidationError(f"product: {item} - is out of Stock")
        return cart

    def calculate_total(self, cart):
        total_price = 0
        breakdown = {}

        for item, quantity in cart.items():
            product = Product.objects.get(name=item)
            discount = Discount.objects.filter(product=product).first()
            subtotal = quantity * product.price

            if discount and quantity >= discount.min_discount_quantity:
                discount_groups = quantity // discount.min_discount_quantity
                remainder = quantity % discount.min_discount_quantity
                subtotal = (discount_groups * discount.discount_price) + (remainder * product.price)

            breakdown[item] = {"quantity": quantity, "subtotal": subtotal}
            total_price += subtotal

        return total_price, breakdown