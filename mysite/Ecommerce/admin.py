from django.contrib import admin

from .models import (Order, Category, Product, OrderItem, Photo)

admin.site.register(Order)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(OrderItem)
admin.site.register(Photo)

