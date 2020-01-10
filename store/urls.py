from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('admin_products/upload/',upload),
    path('admin_products/upload/save/',uploaded_save),
    
]



