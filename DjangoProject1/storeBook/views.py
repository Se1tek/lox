from rest_framework import viewsets
from .models import Category, Book, Cart, CartItem, Order, OrderItem
from .serializers import (
    CategorySerializer, BookSerializer,
    CartSerializer, CartItemSerializer,
    OrderSerializer, OrderItemSerializer
)
from django.shortcuts import render
de

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
def catalog_view(request):
    return render(request, 'catalog.html')