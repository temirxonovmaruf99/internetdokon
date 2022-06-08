import django_filters

from main.models import Product


class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = {
            'price': ['lt', 'gt']
        }


class ProductFilterName(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = {
            'name': ['lt', 'gt']
        }
