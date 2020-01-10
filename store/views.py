from django.shortcuts import render
from store.models import *
from django.http import *
from django.db.models import Q
from django.contrib import messages
from django.core.files.storage import FileSystemStorage

# Create your views here.

def upload(request):
    return render(request,'CRUD_Inventory/upload.html')
    
def uploaded_save(request):
    getall=request.POST
    name=request.POST['Product_Name']
    typ=request.POST['Product_Type']
    price=request.POST['Product_Price']
    qty=request.POST['Product_Quantity']

    product.objects.create(Product_Name=name, Product_Type=typ,Product_Price=price,Product_Quantity=qty)
    return HttpResponseRedirect('/store/admin_products/')


