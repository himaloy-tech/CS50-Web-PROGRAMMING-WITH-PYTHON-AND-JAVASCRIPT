from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("details/<int:id>", views.details, name="details"),
    path('create_listings', views.create_listings, name="create_listings")
]
