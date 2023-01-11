from rest_framework import  serializers
from apps.products.models import Product

class PoductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class ProductUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

