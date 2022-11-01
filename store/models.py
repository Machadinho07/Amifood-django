from audioop import reverse
from distutils.command.upload import upload
from email.mime import audio
from email.policy import default
from enum import unique
from itertools import product
from unicodedata import name
from django.db import models
from category.models import Category
from django.urls import reverse

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length= 50, unique = True)
    slug = models.CharField(max_length=200, unique = True)
    description = models.TextField(max_length = 500, blank = True)
    price = models.IntegerField()
    image = models.ImageField(upload_to = 'photos/products')
    stock = models.IntegerField()
    is_available = models.BooleanField(default = True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['-id']


    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.name