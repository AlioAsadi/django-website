from django.db.models import Q
from django.views.generic import ListView, DetailView
from .models import Category, Product
from .forms import SearchForm

class CategoryListView(ListView):
    template_name = "catalog/category_list.html"
    context_object_name = "categories"

    def get_queryset(self):
        return Category.objects.filter(is_active=True)


class ProductListView(ListView):
    template_name = "catalog/product_list.html"
    context_object_name = "products"
    paginate_by = 12

    def get_queryset(self):
        qs = Product.objects.select_related("category").prefetch_related("inventory").filter(is_active=True)

        self.form = SearchForm(self.request.GET)
        self.form.is_valid()

        q = self.form.cleaned_data.get("q")
        stock = self.form.cleaned_data.get("stock")
        sort = self.form.cleaned_data.get("sort") or "new"

        if hasattr(self, "category") and self.category:
            qs = qs.filter(category=self.category)

        if q:
            qs = qs.filter(Q(name__icontains=q) | Q(description__icontains=q))

        if stock:
            qs = qs.filter(inventory__status=stock)

        if sort == "name":
            qs = qs.order_by("name")
        else:
            qs = qs.order_by("-updated_at")

        return qs

    def dispatch(self, request, *args, **kwargs):
        self.category = None
        slug = kwargs.get("slug")
        if slug:
            self.category = Category.objects.filter(slug=slug, is_active=True).first()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["category"] = self.category
        ctx["form"] = getattr(self, "form", SearchForm())
        ctx["q"] = self.request.GET.get("q", "")
        ctx["stock"] = self.request.GET.get("stock", "")
        ctx["sort"] = self.request.GET.get("sort", "new")
        return ctx


class ProductDetailView(DetailView):
    template_name = "catalog/product_detail.html"
    context_object_name = "product"

    def get_queryset(self):
        return Product.objects.select_related("category").prefetch_related("inventory").filter(is_active=True)
