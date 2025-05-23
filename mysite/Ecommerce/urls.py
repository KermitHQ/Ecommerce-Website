from .views import (ProductDeleteView, CategoryCreationView,AvailableItemsList,
  CartView, AddProduct, increaseQuantity, decreaseQuantity,deleteOrderItem, ProductCreateView, makeOrder, cancelOrder, OrderListView,

	)


from django.urls import path

urlpatterns = [
    path('<int:page>', AvailableItemsList, name="home-paginated"),
    path('', AvailableItemsList, name="home"),
    path('category/<str:category>/', AvailableItemsList, name="home"),



    path('orders/', OrderListView, name="order-list"),


   
    path('create_product/',  ProductCreateView, name="create-new-product"),
    path('create_category/', CategoryCreationView, name="create-category"),

    path('product/<int:product_id>/delete/', ProductDeleteView, name="delete-product"),

    path('addproduct/', AddProduct, name='add-product'),
    path('cart/', CartView, name="cart"),
    path('cart/increase/', increaseQuantity, name='increase'),
    path('cart/decrease/', decreaseQuantity, name='decrease'),

  

    path('makeorder/<int:order_id>/', makeOrder, name='make-order'),
    path('cancelorder/<int:order_id>/', cancelOrder, name='cancel-order'),

    path('cart/delete-orderitem/<int:orderitem_id>/', deleteOrderItem, name='delete-orderitem'),

]
