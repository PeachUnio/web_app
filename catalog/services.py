from config.settings import CACHE_ENABLED
from catalog.models import Product
from django.core.cache import cache


def get_products_from_cache():
    """Получает данные о продукте из кеша, если он пуст, делает запрос бд"""
    if not CACHE_ENABLED:
        return Product.objects.filter(publish_product=True).order_by('name', 'category', 'cost')
    key = "products_list"
    products = cache.get(key)
    if products is not None:
        return products
    products = Product.objects.filter(publish_product=True).order_by('name', 'category', 'cost')
    cache.set(key, products)
    return products
