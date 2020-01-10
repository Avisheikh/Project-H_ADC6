from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('', store , name='store'),
    path('admin_products/',admin_page, name='admin'),
    path("admin_products/search/", search),
]



