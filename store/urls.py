from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('', store , name='store'),# store page
    path("admin_products/restricted/",admin_restricted),# Restricted page only authorized user can view the page
    path('admin_products/',admin_page, name='admin'),# Manage Product Page
    path('admin_products/upload/',upload),# Page where you can upload products
    path('admin_products/upload/save/',uploaded_save),# saves product which are uploaded in database
    path('admin_products/edit/<int:id>',get_product),# Update form page for selected product
    path('admin_products/edit/update/<int:id>', update_product),# saves update form of selected product
    path('admin_products/delete/<int:id>', delete_product),# delete selected product
    path("admin_products/search/", search),# search the product which are in manage prodct page
    path("search/",store_search),#search in store page
    path('admin_products/uploaded_file/',upload_list),#page to uploaded file
    path('admin_products/upload_file/',upload_file),#upload file
    path("admin_products/uploaded_file/delete/<int:id>", delete),#delete selected file
    path("page/<int:pageNo>/",pagination),#pagination for store page
    path("admin_products/page/<int:pageNo>/",paginationForCRUD)#pagination for admin page
    
]



