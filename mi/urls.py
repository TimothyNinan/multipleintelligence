from django.urls import path
from . import views

urlpatterns = [
    path("login", views.login_view, name="login"),
    path("register", views.register_view, name="register"),
    path("logout", views.logout_view, name="logout"),
    path("test", views.test_view, name="test"),
    path("favicon.ico", views.favicon_view),
    path("test/<str:code>", views.test_code, name="testcode"),
    path("scores/<str:code>", views.scores, name="scores"),
    path("dash", views.dash, name="dash"),
    path("classes/<str:code>", views.classes, name="classes"),
    path("", views.index, name="index"),
]