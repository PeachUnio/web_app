from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from blog.models import Publication


class MainView(ListView):
    model = Publication
    template_name = "main_page.html"


class PublicationsDitail(DetailView):
    model = Publication
    template_name = "publication_ditail.html"
    context_object_name = "publication"

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class PublicationCreateView(CreateView):
    model = Publication
    template_name = "blog_form.html"
    fields = "title", "content", "image"
    success_url = reverse_lazy("blog:main_page")


class PublicationUpdateView(UpdateView):
    model = Publication
    template_name = "blog_form.html"
    fields = "title", "content", "image"
    success_url = reverse_lazy("blog:main_page")

    def get_success_url(self):
        return reverse("blog:publications_ditail", args=[self.kwargs.get("pk")])


class PublicationDeleteView(DeleteView):
    model = Publication
    template_name = "publication_confirm_del.html"
    success_url = reverse_lazy("blog:main_page")
    context_object_name = "publication"
