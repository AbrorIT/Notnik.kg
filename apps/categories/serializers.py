from rest_framework import serializers
from apps.categories.models import Category
from apps.products.serializers import ProductSerializer



class CategorySerializer(serializers.ModelSerializer):
    category = ProductSerializer(read_only = True, many = True)
    class Meta:
        model  = Category
        fields = "__all__"

class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class CategoryUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"