from django.shortcuts import render
from rest_framework import generics
from apps.products.serializers import ProductSerializer,ProductCreateSerializer,ProductUpdateSerializer
from apps.products.models import Product

# Create your views here.

class ProductAPIView(generics.ListAPIView):
    gueryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductCreateAPIView(generics.CreateAPIView):
    gueryset = Product.objects.all()
    serializer_class = ProductCreateSerializer

class ProductUpdateAPIView(generics.UpdateAPIView):
    gueryset = Product.objects.all()
    serializer_class = ProductUpdateSerializer
    
class ProductDeleteAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    