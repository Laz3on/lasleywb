from django.urls import path

from . import views

urlpatterns = [
    path("", views.jokes, name="jokes"),
    path("jokes/", views.jokes, name="jokes"),
]
