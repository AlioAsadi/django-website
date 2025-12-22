from django.contrib import admin
from .models import Category, Product, Inventory

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "parent", "is_active", "sort_order")
    list_filter = ("is_active",)
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}

class InventoryInline(admin.StackedInline):
    model = Inventory
    extra = 0

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "is_active", "updated_at")
    list_filter = ("is_active", "category")
    search_fields = ("name", "description", "sku", "brand")
    prepopulated_fields = {"slug": ("name",)}
    inlines = [InventoryInline]
