import django_filters
from .models import ProductModel


class ProductFilter(django_filters.FilterSet):
    seller = \
        django_filters.CharFilter(field_name='seller__username', lookup_expr='iexact')

    class Meta:
        model = ProductModel
        fields = ['seller']
