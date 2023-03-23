from django.urls import path
from django.contrib import admin
from board import views

urlpatterns = [
    path('', views.index, name="index"),
    path('cal', views.calculate, name="calculate"),
    path('get_ans', views.get_ans, name="get_ans")
]