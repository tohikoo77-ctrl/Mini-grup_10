from dataclasses import field
from re import search

import django_filters
from django.db.models import Q

from ..models import Product, Category


class ProductFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(
        field_name='name',
        lookup_expr='icontains',
        label='Qidiruv'
    )

    price_min = django_filters.NumberFilter(
        field_name="price",
        lookup_expr="gte",
        label="Minimal narx"
    )

    price_max = django_filters.NumberFilter(
        field_name="price",
        lookup_expr="lte",
        label="Maksimal narx"
    )


    categoriya = django_filters.ModelChoiceFilter(
        queryset=Category.objects.all(),
        field_name="category",
        label="kategoriya"
    )


    brand = django_filters.CharFilter(lookup_expr="iexact")

    class Meta:
        model = Product
        field = ["search", "price_min", "price_max", "categoriya", "brand"]


    def filter_search(self, queryset, name, value):
        if value:
            return queryset.filter(
                Q(name__icontains=value),
                Q(description_icontains=value)
            )
        return queryset