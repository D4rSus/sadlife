from django.db import models
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    ordering = ('name',)
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название')
    slug = models.SlugField(max_length=20, unique=True, verbose_name='Сокр. название')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('bike:product_list_by_category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, verbose_name='Категория')
    name = models.CharField(max_length=100, db_index=True, verbose_name='Название')
    slug = models.SlugField(max_length=100,db_index=True, unique=True, verbose_name='Сокр. название')
    image = models.ImageField(upload_to="static/img/db/", blank=True, verbose_name='Изображение')
    description = models.TextField(max_length=100, blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    available = models.BooleanField(default=True, verbose_name='В продаже')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата последнего обновления')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        index_together = (('id', 'slug'), )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('bike:product_details', args=[self.id, self.slug])


class AdditionalProductImage(models.Model):
    image = models.ImageField(upload_to='products/%Y/%m/%d', verbose_name='Изображение')
    product = models.ForeignKey(Product, related_name='additional_images', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Дополнительное изображение'
        verbose_name_plural = 'Дополнительные изображения'
