from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, TemplateView, DetailView

from catalog.models import Product


class HomeView(ListView):
    model = Product
    template_name = "catalog/home.html"


class ContactsView(TemplateView):
    template_name = "catalog/contacts.html"


class ProductsDitail(DetailView):
    model = Product
    template_name = "catalog/products_ditail.html"
    context_object_name = "product"
