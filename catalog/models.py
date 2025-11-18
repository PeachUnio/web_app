from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование продукта", help_text="Введите наименование продукта")
    description = models.TextField(verbose_name="Описание продукта", help_text="Введите описание продукта")
    image = models.ImageField(upload_to="catalog/image", blank=True, null=True, verbose_name="Изображение", help_text="Загрузите фото продукта")
    category = models.ForeignObject(Category, on_delete=models.CASCADE)
    cost = models.IntegerField(verbose_name="Цена")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата последнего изменения")

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "category", "cost"]

    def __str__(self):
        return self.name

