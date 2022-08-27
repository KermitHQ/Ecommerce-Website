from .views import (ProductDeleteView, CategoryCreationView,AvailableItemsList,
  CartView, AddProduct, increaseQuantity, decreaseQuantity,deleteOrderItem, CreateNewProductView, ImagesView
	)


from django.urls import path

urlpatterns = [
    path('', AvailableItemsList, name="home"),
    path('category/<str:category>/', AvailableItemsList, name="home"),
   

    path('create_product/', CreateNewProductView, name="create-new-product"),


    path('images/', ImagesView, name="index2"),
    
    path('create_category/', CategoryCreationView, name="create-category"),
    path('product/<int:product_id>/delete/', ProductDeleteView, name="delete-product"),
    path('addproduct/', AddProduct, name='add-product'),

     path('cart/', CartView, name="cart"),
    path('cart/increase/', increaseQuantity, name='increase'),
    path('cart/decrease/', decreaseQuantity, name='decrease'),
    path('cart/delete-orderitem/<int:orderitem_id>/', deleteOrderItem, name='delete-orderitem'),
   
]
