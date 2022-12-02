"""Url configuration for bts_info app."""

from django.urls import path

from . import views

urlpatterns = [
    path('', views.bts_info, name='bts-info'),
]
