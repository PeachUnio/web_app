from config.settings import CACHE_ENABLED
from catalog.models import Product, Category
from django.core.cache import cache
from django.db import models


def get_products_from_cache():
    """Получает данные о продукте из кеша, если он пуст, делает запрос бд"""
    if not CACHE_ENABLED:
        return Product.objects.filter(publish_product=True).order_by('name', 'category', 'cost')
    key = "products_list"
    products = cache.get(key)
    if products is not None:
        return products
    products = Product.objects.filter(publish_product=True).order_by('name', 'category', 'cost')
    cache.set(key, products, 60 * 15)
    return products


def get_products_by_category(category_id):
    """Получает всех продукты в указанной категории"""
    if not CACHE_ENABLED:
        return _get_fresh_products_by_category(category_id)

    cache_key = f"products_by_category_id_{category_id}"
    products = cache.get(cache_key)

    if products is not None:
        return products

    products = _get_fresh_products_by_category(category_id)
    cache.set(cache_key, products, 60 * 15)
    return products


def _get_fresh_products_by_category(category_id):
    """Получение свежих данных из бд без кеширования"""
    try:
        category = Category.objects.get(id=category_id)
        return Product.objects.filter(
            category=category,
            publish_product=True
        ).select_related('category').order_by('name', 'cost')
    except Category.DoesNotExist:
        return Product.objects.none()
