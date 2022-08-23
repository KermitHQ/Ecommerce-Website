from .views import (ProductListView, ProductCreationView, ProductDeleteView, CategoryCreationView
	)

from django.urls import path

urlpatterns = [
    path('', ProductListView.as_view(), name="home"),
    path('create_product/', ProductCreationView, name="create-product"),
    path('create_category/', CategoryCreationView, name="create-category"),
    path('product/<int:product_id>/delete/', ProductDeleteView, name="delete-product"),
]
