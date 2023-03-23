from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("jing", views.jing, name="jing"),
    path("venti", views.venti, name="venti"),
    path("<str:name>", views.greet, name="greet")
]
