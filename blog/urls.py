from django.urls import path, include
from blog.apps import BlogConfig
from blog.views import MainView, PublicationsDitail, PublicationCreateView, PublicationUpdateView


app_name = BlogConfig.name

urlpatterns = [
   path("", MainView.as_view(), name="main_page"),
   path("publication/<int:pk>/", PublicationsDitail.as_view(), name="publications_ditail"),
   path("create/", PublicationCreateView.as_view(), name="create"),
   path("publication/<int:pk>/update/", PublicationUpdateView.as_view(), name="publications_update"),
]