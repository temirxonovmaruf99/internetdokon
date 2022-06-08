from django.urls import path
from .views import About_main, Index_main, Testimonial_main, Why_main, ProductWiew


from .views import ProductInfo


app_name = 'main'

urlpatterns = [
    path('', Index_main, name="index"),
    path('about/', About_main.as_view(), name="about"),
    path('product/', ProductWiew.as_view(), name="product"),
    path('test/', Testimonial_main.as_view(), name="test"),
    path('why/', Why_main.as_view(), name="why"),

    path('product_info-<int:pk>/', ProductInfo.as_view(), name="product_info"),
]