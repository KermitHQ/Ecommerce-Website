from .views import ( ProductCreationView, ProductDeleteView, CategoryCreationView,AvailableItemsList
	)

from django.urls import path

urlpatterns = [
    path('', AvailableItemsList, name="home"),
    path('category/<str:category>/', AvailableItemsList, name="home"),

    path('create_product/', ProductCreationView, name="create-product"),
    path('create_category/', CategoryCreationView, name="create-category"),
    path('product/<int:product_id>/delete/', ProductDeleteView, name="delete-product"),
]
