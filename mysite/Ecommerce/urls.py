from .views import (ProductListView, ProductCreationView, ProductDeleteView
	)

from django.urls import path

urlpatterns = [
    path('', ProductListView.as_view(), name="home"),
    path('create_product/', ProductCreationView, name="create-product"),
    path('product/<int:product_id>/delete/', ProductDeleteView, name="delete-product")
]
