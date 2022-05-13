"""Dishes API URL Configuration"""
from django.urls import path

from .views import FoodCategoryAPIView

urlpatterns = [
    path('foods/', FoodCategoryAPIView.as_view(), name='Food')
]
