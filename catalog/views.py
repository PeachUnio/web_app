from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse

from catalog.models import Product
from catalog.forms import ProductForm


class HomeView(ListView):
    model = Product
    template_name = "catalog/home.html"


class ContactsView(TemplateView):
    template_name = "catalog/contacts.html"


class ProductsDitail(DetailView):
    model = Product
    template_name = "catalog/products_ditail.html"
    context_object_name = "product"


class ProductsCreateView(CreateView):
    model = Product
    template_name = "catalog/product_form.html"
    form_class = ProductForm
    success_url = reverse_lazy("catalog:home")


class ProductUpdateView(UpdateView):
    model = Product
    template_name = "catalog/product_form.html"
    form_class = ProductForm
    success_url = reverse_lazy("catalog:home")

    def get_success_url(self):
        return reverse("catalog:products_ditail", args=[self.kwargs.get("pk")])


class ProductDeleteView(DeleteView):
    model = Product
    template_name = "catalog/product_confirm_del.html"
    success_url = reverse_lazy("catalog:home")
    context_object_name = "product"
