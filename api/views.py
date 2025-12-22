from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from django.db.models import Q
from catalog.models import Product
from .serializers import ProductSerializer

@api_view(["GET"])
def health(request):
    return Response({"status": "ok"})

class ProductSearchApi(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        qs = Product.objects.select_related("category").prefetch_related("inventory").filter(is_active=True)
        q = self.request.GET.get("q")
        if q:
            qs = qs.filter(Q(name__icontains=q) | Q(description__icontains=q))
        return qs.order_by("-updated_at")[:50]
