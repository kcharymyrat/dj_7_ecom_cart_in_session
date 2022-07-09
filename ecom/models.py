from unicodedata import category
from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class ProductManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, db_index=True)
    slug = models.SlugField(max_length=120, unique=True)

    class Meta:
        verbose_name_plural = "categories"


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, unique=True, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    in_stock = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = models.Manager()
    actives = ProductManager()
