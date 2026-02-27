from rest_framework import serializers
from .models import InventoryItem, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']


class InventorySerializer(serializers.ModelSerializer):
    # Nested category details (read-only)
    category_details = CategorySerializer(source='category', read_only=True)

    class Meta:
        model = InventoryItem
        fields = [
            'id',
            'name',
            'description',
            'quantity',
            'price',
            'category',          # For POST (send category ID)
            'category_details',  # For GET (shows full category info)
            'created_at',
            'updated_at'
        ]

    def validate_quantity(self, value):
        if value < 0:
            raise serializers.ValidationError("Quantity cannot be negative.")
        return value

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than zero.")
        return value
