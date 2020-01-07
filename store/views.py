from django.shortcuts import render
from store.models import product
from django.http import HttpResponse

# Create your views here.
def store(request):
    return render(request,'store.html')

def admin_page(request):
    obj=product.objects.all()  
    return render(request,'Admin_CRUD_Products.html',{'product':obj})

def upload(request):
    return render(request,'CRUD_Inventory/upload.html')
    
def uploaded_save(request):
    getall=request.POST
    name=request.POST['Product_Name']
    typ=request.POST['Product_Type']
    price=request.POST['Product_Price']
    qty=request.POST['Product_Quantity']

    product.objects.create(Product_Name=name, Product_Type=typ,Product_Price=price,Product_Quantity=qty)
    obj=product.objects.all()
    return render(request,'Admin_CRUD_Products.html',{'product':obj})