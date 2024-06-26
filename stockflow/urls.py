"""
URL configuration for stockflow project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from .views import EstoqueListView, estoque_detail, get_stocks, get_stock, create_stock, delete_stock, update_stock

urlpatterns = [
    path('admin/', admin.site.urls),
    path('estoques/', EstoqueListView.as_view(), name='estoque-list'),
    path('estoques/<int:pk>/', estoque_detail, name='estoque_detail'),
    path('api/estoques/', get_stocks, name='get_stocks'),
    path('api/estoque/<int:pk>', get_stock, name='get_stock'),
    path('api/estoques/create/', create_stock, name='create_stock'),
    path('api/estoques/<int:pk>/delete/', delete_stock, name='delete_stock'),
    path('api/estoques/<int:pk>/update/', update_stock, name='update_stock'),
]
