from django.urls import path
from .views import fetch_recipe

urlpatterns = [
    path("fetch_recipe/", fetch_recipe, name="fetch_recipe"),
]
