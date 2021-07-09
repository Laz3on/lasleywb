from django.urls import path

from . import views

urlpatterns = [
    path('', views.dadjoke, name='dadjoke'),
    path('hello', views.hello, name='hello'),
]
