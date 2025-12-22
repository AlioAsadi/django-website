from django.views.generic import ListView, DetailView
from .models import Article

class ArticleListView(ListView):
    template_name = "articles/article_list.html"
    context_object_name = "articles"
    paginate_by = 10

    def get_queryset(self):
        return Article.objects.filter(is_published=True)

class ArticleDetailView(DetailView):
    template_name = "articles/article_detail.html"
    context_object_name = "article"

    def get_queryset(self):
        return Article.objects.filter(is_published=True)
