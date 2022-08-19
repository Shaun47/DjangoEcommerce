from django.urls import reverse
from django.db import models
from tabnanny import verbose

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100,unique=True)
    description = models.TextField(blank=True)
    cat_img = models.ImageField(max_length=255,upload_to="photos/categories", blank=True)

    class Meta:
        verbose_name: 'category'
        verbose_name_plural: 'Categories'

    def get_url(self):
        return reverse('products_by_category',args=[self.slug])

    def __str__(self):
        return self.category_name 