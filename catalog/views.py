from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import models

from catalog.models import Product, Category
from catalog.forms import ProductForm, ProductModerForm
from catalog.services import get_products_from_cache, get_products_by_category


class HomeView(ListView):
    model = Product
    template_name = "catalog/home.html"

    def get_queryset(self):
        return get_products_from_cache()


class ContactsView(TemplateView):
    template_name = "catalog/contacts.html"


class ProductsDitail(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "catalog/products_ditail.html"
    context_object_name = "product"


class ProductsCreateView(LoginRequiredMixin, CreateView):
    model = Product
    template_name = "catalog/product_form.html"
    form_class = ProductForm
    success_url = reverse_lazy("catalog:home")

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    template_name = "catalog/product_form.html"
    form_class = ProductForm
    success_url = reverse_lazy("catalog:home")

    def get_success_url(self):
        return reverse("catalog:products_ditail", args=[self.kwargs.get("pk")])

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm("catalog.can_unpublish_product") and user.has_perm("catalog.delete_product"):
            return ProductModerForm
        raise PermissionDenied


class ProductDeleteView(DeleteView):
    model = Product
    template_name = "catalog/product_confirm_del.html"
    success_url = reverse_lazy("catalog:home")
    context_object_name = "product"

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        user = request.user

        if user == self.object.owner:
            return super().dispatch(request, *args, **kwargs)

        if user.has_perm("catalog.can_unpublish_product") and user.has_perm("catalog.delete_product"):
            return super().dispatch(request, *args, **kwargs)

        raise PermissionDenied


class CategoryProductsView(ListView):
    template_name = "catalog/category_products.html"
    context_object_name = "products"

    def get_queryset(self):
        category_id = self.kwargs["category_id"]
        return get_products_by_category(category_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.kwargs["category_id"]
        context["category"] = get_object_or_404(Category, id=category_id)
        return context


class CategoryListView(ListView):
    model = Category
    template_name = "catalog/category_list.html"
    context_object_name = "categories"

    queryset = Category.objects.all().order_by("name")