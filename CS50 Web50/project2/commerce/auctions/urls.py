from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create_listing", views.create_listing, name="create_listing"),
    path('categories_list', views.categories_list, name='categories_list'),
    path("auction_diaplay/<int:auction_id>", views.auction_display, name="auction_display"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("category_display/<int:category_id>", views.category_display, name="category_display"),
]
