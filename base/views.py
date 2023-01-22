from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .products import products

# Create your views here.
@api_view(['GET'])
def getRoutes(request):

  routes = [
    '/api/products',
    '/api/products/create',

    '/api/products/upload',

    '/api/products/<id>/reviews',

    '/api/products/top',
    '/api/products/<id>/',

    '/api/products/delete/<id>',
    '/api/products/update/<id>'
  ]

  return Response(routes)

@api_view(['GET'])
def getProducts(request):
  return Response(products)

@api_view(['GET'])
def getProductById(request, primaryKey):
  if primaryKey not in products:
    return Response("Product Not Found", status=404)
  return Response(products[primaryKey])