from .views import ( ProductCreationView, ProductDeleteView, CategoryCreationView,AvailableItemsList, CartView, AddProduct,
	)


from django.urls import path

urlpatterns = [
    path('', AvailableItemsList, name="home"),
    path('category/<str:category>/', AvailableItemsList, name="home"),
    path('cart/', CartView, name="cart"),
    
    

    path('create_product/', ProductCreationView, name="create-product"),
    path('create_category/', CategoryCreationView, name="create-category"),
    path('product/<int:product_id>/delete/', ProductDeleteView, name="delete-product"),
    path('addproduct/', AddProduct, name='add-product'),
   
]
