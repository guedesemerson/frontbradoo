from .views import (listProduct,
                    newProduct,
                    ProductDelete,
                    updateProduct,
                    formUpdateProduct)
from django.urls import path


urlpatterns = [
    path('index/<id>', listProduct, name='products'),
    path('add_update_product/<id>', updateProduct, name='updateproduct'),
    path('update_product/<id>', formUpdateProduct, name='formupdateproduct'),
    path('new_product/<id>', newProduct, name='newproduct'),
    path('delete_product/<id>', ProductDelete, name='deleteproduct')


]