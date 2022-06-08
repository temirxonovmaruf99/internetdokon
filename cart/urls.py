from django.urls import path
from .views import cart_add, cart_list, cart_checkout

app_name = 'cart'

urlpatterns = [
    path('cart_add/<str:action>-<int:pid>/', cart_add, name="cart_add"),
    path('cart/', cart_list, name="cart"),
    path('buyurtma/', cart_checkout, name="buyurtma")
]