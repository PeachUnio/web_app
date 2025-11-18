from django.db import models


class Product(models.Model):
    name = models.CharField(
        max_length=100, verbose_name="Наименование продукта", help_text="Введите наименование продукта"
    )
    description = models.TextField(
        blank=True, null=True, verbose_name="Описание продукта", help_text="Введите описание продукта"
    )
    image = models.ImageField(
        upload_to="catalog/image",
        blank=True,
        null=True,
        verbose_name="Изображение",
        help_text="Загрузите фото продукта",
    )
    category = models.ForeignKey(
        on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Категория", related_name="products"
    )
    cost = models.IntegerField(verbose_name="Цена")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата последнего изменения")

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "category", "cost"]

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(
        max_length=100, verbose_name="Наименование категория", help_text="Введите наименование категории"
    )
    description = models.TextField(
        blank=True, null=True, verbose_name="Описание категории", help_text="Введите описание категории"
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name
