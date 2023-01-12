"""notnik URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from apps.products.views import ProductAPIView, ProductCreateAPIView, ProductUpdateAPIView, ProductDeleteAPIView
from apps.categories.views import CategoryAPIView,CategoryCreateAPIView, CategoryUpdateAPIView, CategoryDeleteAPIView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    #продукт api
    path('api/product', ProductAPIView.as_view(), name="product_api"),
    path('api/product/create', ProductCreateAPIView.as_view(), name = "post_create_api"),
    path('api/product/update/<int:pk>', ProductUpdateAPIView.as_view(), name = "post_api_update"),
    path('api/product/delete/<int:pk>',ProductDeleteAPIView.as_view(),name = "product_api_delete"),

    #категории api
    path('api/categories',CategoryAPIView.as_view(),name = "category_api"),
    path('api/category/create',CategoryCreateAPIView.as_view(),name = "category_create_api"),
    path('api/category/update/<int:pk>',CategoryUpdateAPIView.as_view(),name = "category_api_update"),
    path('api/category/delete/<int:pk>',CategoryDeleteAPIView.as_view(),name = "category_api_delete"),
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)