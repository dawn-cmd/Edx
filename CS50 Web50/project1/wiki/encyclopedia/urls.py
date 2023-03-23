from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("creat", views.creat, name="creat"),
    path("rand", views.randpage, name="rand"),
    path("search", views.search, name="search"),
    path("edit/<str:title>", views.edit, name="edit"),
    path("wiki/<str:title>", views.entry, name="entry"),
]
