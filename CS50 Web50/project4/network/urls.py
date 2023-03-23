
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path('profile/<str:name>', views.profile, name="profile"),
    path('edit/<int:id>', views.edit, name="edit"),
    path('following', views.following, name="following"),

    path('post', views.post, name="post"),
    path('posts', views.posts, name="posts"),
    path('maxpage', views.maxpage, name="maxpage"),
    path('get_follow', views.get_follow, name="get_follow"),
    path('has_followed', views.has_followed, name="has_followed"),
    path('become_followed', views.become_followed, name="become_followed"),
    path('like', views.like, name="like"),
    path('get_like', views.get_like, name="get_like"),
]
