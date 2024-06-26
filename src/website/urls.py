from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("catalog/", views.catalog, name="catalog"),
    path("search/", views.search, name="search"),
]
