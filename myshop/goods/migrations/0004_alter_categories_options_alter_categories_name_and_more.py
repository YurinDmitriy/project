# Generated by Django 5.1.1 on 2024-09-23 08:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_alter_categories_options_products'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categories',
            options={'verbose_name': 'Категорию', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterField(
            model_name='categories',
            name='name',
            field=models.CharField(max_length=150, unique=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='categories',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True, unique=True, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.categories', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='products',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='products',
            name='discount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=7, verbose_name='Скидка в %'),
        ),
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='goods_images', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='products',
            name='name',
            field=models.CharField(max_length=150, unique=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=7, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='products',
            name='quantity',
            field=models.PositiveIntegerField(default=0, verbose_name='Количество'),
        ),
        migrations.AlterField(
            model_name='products',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True, unique=True, verbose_name='URL'),
        ),
        migrations.AlterModelTable(
            name='categories',
            table='category',
        ),
        migrations.AlterModelTable(
            name='products',
            table='product',
        ),
    ]
