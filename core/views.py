from django.shortcuts import render
from catalog.models import Category, Product
from django.db.models import Count, Q

def home(request):
    categories = (
        Category.objects.filter(is_active=True)
        .annotate(products_count=Count("products", filter=Q(products__is_active=True)))
        .order_by("sort_order", "name")[:12]
    )

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
    return render(request, "core/about.html")

def contact(request):
    return render(request, "core/contact.html")

def handle_404(request, exception):
    return render(request, "404.html", status=404)