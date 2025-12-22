from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    parent = models.ForeignKey("self", null=True, blank=True, related_name="children", on_delete=models.PROTECT)
    is_active = models.BooleanField(default=True)
    sort_order = models.PositiveIntegerField(default=0)
    
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="categories/", blank=True, null=True)

    class Meta:
        ordering = ["sort_order", "name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("catalog:category_products", kwargs={"slug": self.slug})


class StockStatus(models.TextChoices):
    IN_STOCK = "in_stock", _("موجود")
    LIMITED = "limited", _("محدود")
    OUT_OF_STOCK = "out_of_stock", _("ناموجود")


class Product(models.Model):
    category = models.ForeignKey(Category, related_name="products", on_delete=models.PROTECT)
    name = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)

    # optional fields (helpful)
    sku = models.CharField(max_length=80, blank=True)
    brand = models.CharField(max_length=120, blank=True)

    image = models.ImageField(upload_to="products/", blank=True, null=True)

    # since you are a catalog, price can be optional
    price = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    call_for_price = models.BooleanField(default=True)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-updated_at", "name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("catalog:product_detail", kwargs={"slug": self.slug})


class Inventory(models.Model):
    product = models.OneToOneField(Product, related_name="inventory", on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=StockStatus.choices, default=StockStatus.IN_STOCK)
    quantity = models.PositiveIntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product.name} -> {self.get_status_display()}"
    
    