from django.urls import path
from .views import ProductListView, DiscountListView, CartItemView, CheckoutView

urlpatterns = [
    path("products/", ProductListView.as_view(), name="product-list"),
    path("discounts/", DiscountListView.as_view(), name="discount-list"),
    path("cart/", CartItemView.as_view(), name="cart-list"),
    path("checkout/", CheckoutView.as_view(), name="checkout"),
]
