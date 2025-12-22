from django.urls import path
from .views import health, ProductSearchApi

urlpatterns = [
    path("health/", health, name="api-health"),
    path("products/search/", ProductSearchApi.as_view(), name="api-product-search"),
]
