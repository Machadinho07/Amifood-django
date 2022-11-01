from audioop import reverse
from distutils.command.upload import upload
from django.urls import reverse
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=30, blank=True)
    slug = models.CharField(max_length=100, unique = True)
    image = models.ImageField(upload_to = 'photos/categories', blank = True)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['-id']

    def get_url(self):
        return reverse('products_by_category', args=[self.slug])
        

    def __str__(self):
        return self.name



