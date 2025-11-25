from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, products_ditail

app_name = CatalogConfig.name

urlpatterns = [
    path("", home, name="home"),
    path("contacts/", contacts, name="contacts"),
    path("products/<int:pk>/", products_ditail, name="products_ditail"),
]
