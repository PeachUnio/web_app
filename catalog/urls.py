from django.urls import path, include
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import HomeView, ContactsView, ProductsDitail, ProductsCreateView, ProductUpdateView, ProductDeleteView, CategoryProductsView, CategoryListView

app_name = CatalogConfig.name

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("products/<int:pk>/", cache_page(60 * 15)(ProductsDitail.as_view()), name="products_ditail"),
    path("product/create/", ProductsCreateView.as_view(), name="products_create"),
    path("product/<int:pk>/update/", ProductUpdateView.as_view(), name="products_update"),
    path("product/<int:pk>/delete/", ProductDeleteView.as_view(), name="products_delete"),
    path("categories/", CategoryListView.as_view(), name='category_list'),
    path("category/<int:category_id>/products/", CategoryProductsView.as_view(), name="category_products"),
]
