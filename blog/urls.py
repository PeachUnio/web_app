from django.urls import path, include
from blog.apps import BlogConfig
from blog.views import MainView


app_name = BlogConfig.name

urlpatterns = [
   path("", MainView.as_view(), name="main_page")
]