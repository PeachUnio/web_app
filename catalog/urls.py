from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import HomeView, ContactsView, ProductsDitail, ProductsCreateView

app_name = CatalogConfig.name

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("products/<int:pk>/", ProductsDitail.as_view(), name="products_ditail"),
    path("product/create/", ProductsCreateView.as_view(), name="products_create"),
]
