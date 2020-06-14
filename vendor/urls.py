from .views import (listVendor,
                    newVendor,
                    formNewVendor,
                    vendorDelete,
                    updateVendor,
                    formUpdateVendor)
from django.urls import path


urlpatterns = [
    path('', listVendor, name='vendors'),
    path('add_update_vendor/<id>', updateVendor, name='updatevendor'),
    path('update/<id>', formUpdateVendor, name='formupdate'),
    path('new_vendor', newVendor, name='newvendor'),
    path('form_vendor', formNewVendor, name='formvendor'),
    path('delete_vendor/<id>', vendorDelete, name='deletevendor'),
]