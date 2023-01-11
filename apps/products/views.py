from django.shortcuts import render
from rest_framework import generics
from apps.products.serializers import PoductSerializer,ProductCreateSerializer,ProductUpdateSerializer
from apps.products.models import Product

# Create your views here.

class ProductAPIView(generics.ListAPIView):
    gueryset = Product.objects.all()
    serializer_class = PoductSerializer

class ProductCreateAPIView(generics.CreateAPIView):
    gueryset = Product.objects.all()
    serializer_class = ProductCreateSerializer

class ProductUpdateAPIView(generics.UpdateAPIView):
    gueryset = Product.objects.all()
    serializer_class = ProductUpdateSerializer
    