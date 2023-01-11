from django.db import models
from apps.categories.models import Category

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=255)
    descriptoin = models.TextField()
    image = models.ImageField(upload_to= 'product_image/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name="category")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"