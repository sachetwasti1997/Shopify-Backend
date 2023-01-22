from django.urls import path
from . import views

urlpatterns = [
  path ('', views.getRoutes, name="routes"),
  path ('products/', views.getProducts, name="products"),
  path ('product/<int:primaryKey>/', views.getProductById, name="products")
]