from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Почта")
    phone = models.CharField(max_length=35, verbose_name="Номер телефона", blank=True, null=True)
    avatar = models.ImageField(upload_to="user/avatars/", blank=True, null=True, verbose_name="Аватарка")
    country = models.CharField(max_length=56)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
