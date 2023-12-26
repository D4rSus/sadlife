from django.contrib import admin

from shop.models import Category, Product, AdditionalProductImage


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


class AdditionalImagesInline(admin.TabularInline):
    model = AdditionalProductImage


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', ]
    list_filter = ['category',]
    list_editable = ['price', ]
    inlines = [AdditionalImagesInline]
    prepopulated_fields = {'slug': ('name',)}


