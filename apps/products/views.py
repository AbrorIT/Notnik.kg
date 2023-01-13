from django.shortcuts import render
from rest_framework import generics
from apps.products.serializers import ProductSerializer,ProductCreateSerializer,ProductUpdateSerializer
from apps.products.models import Product
from rest_framework.generics import ListAPIView
from rest_framework import filters

# Create your views here.

class ProductAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer

class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductUpdateSerializer
    
class ProductDeleteAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    

class ProductSearchAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ('product', 'category')