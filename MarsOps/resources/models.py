from django.db import models


class Category(models.Model):
    name = models.CharField('Название', max_length=100)
    slug = models.SlugField('Слаг', unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

class Resources(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='resources')
    title = models.CharField('Название ресурса', max_length=100)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField('Остаток на складе', default=0)
    is_available = models.BooleanField('В продаже', default=True)
    image_path = models.CharField(
        'Путь к картинке',
        max_length=255,
        blank=True,
        help_text='Например: "img/products/pink_bag.jpg"',
    )

    class Meta:
        verbose_name = 'Ресурс'
        verbose_name_plural = 'Ресурсы'

    def __str__(self):
        return f"{self.title} ({self.price})"