from rest_framework import serializers
from catalog.models import Category, Product, Inventory

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ["status", "quantity", "updated_at"]

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "slug", "parent"]

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    inventory = InventorySerializer()

    class Meta:
        model = Product
        fields = ["id", "name", "slug", "description", "price", "call_for_price", "category", "inventory"]
