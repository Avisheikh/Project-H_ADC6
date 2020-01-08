from django.shortcuts import render
from store.models import product
from django.http import HttpResponse

# Create your views here.
def store(request):
    return render(request,'store.html')

def admin_page(request):
    obj=product.objects.all()  
    return render(request,'CRUD_Inventory/Admin_CRUD_Products.html',{'product':obj})

def upload(request):
    return render(request,'CRUD_Inventory/upload.html')
    
def uploaded_save(request):
    getall=request.POST
    name=request.POST['Product_Name']
    typ=request.POST['Product_Type']
    price=request.POST['Product_Price']
    qty=request.POST['Product_Quantity']

    product.objects.create(Product_Name=name, Product_Type=typ,Product_Price=price,Product_Quantity=qty)
    return HttpResponse("Saved")

def get_product(request,id):
    get_id = product.objects.get(id=id)
    return render(request,'CRUD_Inventory/update.html',{'product':get_id})

def update_product(request,id):
    get_id = product.objects.get(id=id)
    get_request = request.POST
    get_id.Product_Name = request.POST['name']
    get_id.Product_Type = request.POST['type']
    get_id.Product_Price = request.POST['price']
    get_id.Product_Quantity = request.POST['qty']
    get_id.save()
    return HttpResponse('Updated')

def delete(request,id):
    get_product = product.object.get(id = id)
    get_product.delete()
    return render(request,'CRUD_Inventory/delete.html')
   
    
   


