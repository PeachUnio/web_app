from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from blog.models import Publication


class MainView(ListView):
    model = Publication
    template_name = "main_page.html"


class PublicationCreateView(CreateView):
    model = Publication
    template_name = "template/blog_create.html"
    fields = "name", "content", "image"
    success_url = reverse_lazy("blog:")
