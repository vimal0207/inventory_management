from rest_framework import serializers
from base.serializers import BaseSerializer
from .models import Product, Category

class CategorySerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = Category

class ProductSerializer(BaseSerializer):
    reason = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'sku', 'quantity', 'price', 'category', 'supplier', 'reason', 'alert_threshold']