from django.contrib import admin
from category.models import Category


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('slug','name')

# Register your models here.

admin.site.register(Category, CategoryAdmin)