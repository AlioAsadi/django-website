from django.urls import path
from .views import CategoryListView, ProductListView, ProductDetailView

app_name = "catalog"

urlpatterns = [
    path("categories/", CategoryListView.as_view(), name="category_list"),
    path("categories/<slug:slug>/", ProductListView.as_view(), name="category_products"),

    path("products/<slug:slug>/", ProductDetailView.as_view(), name="product_detail"),

    # Search uses the same list view (no category)
    path("search/", ProductListView.as_view(), name="search"),
]
