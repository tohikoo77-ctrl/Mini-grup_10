from rest_framework import serializers
from ..models import Product, Category, Firma, Promotion


class ProductListSerializer(serializers.ModelSerializer):

    category_name = serializers.CharField(source='category.name', read_only=True)
    firma_name = serializers.CharField(source='firma.name', read_only=True, allow_null=True)
    promotion_name = serializers.CharField(source='promotion.title', read_only=True, allow_null=True)

    class Meta:
        model = Product
        fields = "__all__"




class ProductDetailSerializer(serializers.ModelSerializer):
    model = Product
    fields = "__all__"
