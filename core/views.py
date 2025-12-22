from django.shortcuts import render
from catalog.models import Category, Product

def home(request):
    categories = Category.objects.filter(is_active=True).order_by("sort_order", "name")[:12]
    featured_products = (
        Product.objects.filter(is_active=True)
        .select_related("category")
        .prefetch_related("inventory")
        .order_by("-updated_at")[:12]
    )
    return render(request, "home.html", {
        "categories": categories,
        "featured_products": featured_products,
    })

def about(request):
    return render(request, "about.html")
