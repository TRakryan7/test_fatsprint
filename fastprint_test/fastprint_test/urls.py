"""
URL configuration for fastprint_test project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from app.controllers import product_controller

urlpatterns = [
    path('', product_controller.produk_list, name='produk-list'),
    path('produk/create', product_controller.produk_create, name='produk-create'),
    path('produk/save', product_controller.produk_save, name='produk-save'),
    path('produk/<int:pk>/edit', product_controller.produk_edit, name='produk-edit'),
    path('produk/<int:pk>/update', product_controller.produk_update, name='produk-update'),
    path('produk/<int:pk>/delete/', product_controller.produk_delete, name='produk-delete'),
    path('produk/generate', product_controller.produk_generate, name='produk-generate'),
]
