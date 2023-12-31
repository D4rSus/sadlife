# Generated by Django 4.2.2 on 2023-06-06 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionalProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='products/%Y/%m/%d', verbose_name='Изображение')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='additional_images', to='shop.product')),
            ],
            options={
                'verbose_name': 'Дополнительное изображение',
                'verbose_name_plural': 'Дополнительные изображения',
            },
        ),
    ]
