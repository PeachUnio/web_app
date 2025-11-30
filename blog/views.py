from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from blog.models import Publication


class MainView(ListView):
    model = Publication
    template_name = "main_page.html"


class PublicationsDitail(DetailView):
    model = Publication
    template_name = "publication_ditail.html"
    context_object_name = "publication"


class PublicationCreateView(CreateView):
    model = Publication
    template_name = "blog_create.html"
    fields = "title", "content", "image"
    success_url = reverse_lazy("blog:main_page")
