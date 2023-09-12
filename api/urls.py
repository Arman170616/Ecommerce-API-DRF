from django.urls import path

from .views import *

urlpatterns = [
    path('products/', api_products),
    path('products/<str:pk>/', api_product),
]

# 1bbe17f8-1f45-463b-9337-817254e295c3