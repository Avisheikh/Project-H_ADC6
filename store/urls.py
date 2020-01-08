from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', store , name='store'),
    path('admin_products/',admin_page, name='admin'),
    path('admin_products/upload/',upload),
    path('admin_products/upload/save/',uploaded_save),
    path('admin_products/edit/<int:id>',get_product),
    path('admin_products/edit/update/<int:id>', update_product),
    path('admin_products/delete/<int:id>', delete)
]

