from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
   
    path('admin_products/edit/<int:id>',get_product),
    path('admin_products/edit/update/<int:id>', update_product),
    path('admin_products/delete/<int:id>', delete_product),
   
    path('admin_products/uploaded_file/',upload_list),
    path('admin_products/upload_file/',upload_file),
    path("admin_products/uploaded_file/delet/<int:id>",run)
]



