from django.urls import path

from . import views

urlpatterns = [
    path('', views.dadjoke, name='dadjoke'),
    # path('/dadjoke', views.dadjoke, name='dadjoke'),
    path('chuck', views.chuck, name='chuck'),
]
