from django.urls import path

urlpatterns = []  # No views yet

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

