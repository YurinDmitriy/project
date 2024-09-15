from django.db import models
from django.db.models import Index
from django.urls import reverse

class Category(models.Model):
    
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])
    
    

class Product(models.Model):
    
    category = models.ForeignKey(Category, on_delete = models.CASCADE, related_name='products')
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

# category : Это ForeignKey модели Category. Это отношение "многие к одному": продукт относится к одной категории, а категория содержит несколько продуктов
# name : Название продукта.
# slug : Алиас продукта(его URL).
# image : Изображение продукта.
# description : Необязательное описание для продукта.
# price : Это поле DecimalField. В нем используется десятичное число Python. Десятичный тип для хранения десятичного числа с фиксированной точностью. Максимальное число цифр (включая десятичные разряды) задается с помощью атрибута max_digits и десятичных знаков с атрибутом decimal_places
# stock : Это поле PositiveIntegerField для хранения остатков данного продукта.
# available : Это булево значение, указывающее, доступен ли продукт или нет. Позволяет включить/отключить продукт в каталоге.
# created : Это поле хранит дату когда был создан объект.
# updated : В этом поле хранится время последнего обновления объекта.

    class Meta:
        ordering = ('name',)
        indexes = [
            Index(fields=['id', 'slug']),
        ]

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])