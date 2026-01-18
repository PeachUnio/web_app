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


def get_products_by_category(category_slug):
    """Получает всех продукты в указанной категории"""
    if not CACHE_ENABLED:
        return _get_fresh_products_by_category(category_slug)

    cache_key = f"products_by_category_{category_slug}"
    products = cache.get(cache_key)

    if products is not None:
        return products

    products = _get_fresh_products_by_category(category_slug)
    cache.set(cache_key, products, 60 * 15)
    return products


def _get_fresh_products_by_category(category_slug):
    """Получение свежих данных из бд без кеширования"""
    try:
        category = Category.objects.get(slug=category_slug)
        return Product.objects.filter(
            category=category,
            publish_product=True
        ).select_related('category').order_by('name', 'cost')
    except Category.DoesNotExist:
        return Product.objects.none()


def get_all_categories_with_counts():
    """Получение всех категорий с количеством опубликованных продуктов"""
    cache_key = "categories_with_counts"

    if not CACHE_ENABLED:
        return _get_fresh_categories_with_counts()

    categories = cache.get(cache_key)
    if categories is not None:
        return categories

    categories = _get_fresh_categories_with_counts()
    cache.set(cache_key, categories, 60 *15)
    return categories


def _get_fresh_categories_with_counts():
    """Получение категорий с подсчетом продуктов из бд"""
    from django.db.models import Count

    return Category.objects.annotate(
        published_products_count=Count(
            'products',
            filter=models.Q(products__publish_product=True)
        )
    ).filter(published_products_count__gt=0).order_by('name')
