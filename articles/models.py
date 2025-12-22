from django.db import models
from django.urls import reverse

class Article(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)
    summary = models.TextField(blank=True)
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to="articles/", blank=True, null=True)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("articles:detail", kwargs={"slug": self.slug})
