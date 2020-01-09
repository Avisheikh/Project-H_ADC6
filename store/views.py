from django.shortcuts import render
from store.models import *
from django.http import *
from django.db.models import Q
from django.contrib import messages
from django.core.files.storage import FileSystemStorage

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
    return HttpResponseRedirect('/store/admin_products/')

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
    return HttpResponseRedirect('/store/admin_products/')

def delete_product(request,id):
    x = product.objects.get(id = id)
    x.delete()
    return HttpResponseRedirect('/store/admin_products/')
   
def search(request):
    if request.method == 'GET':
        search = request.GET['searchs']

        if search:
            match = product.objects.filter(
                Q( Product_Name__icontains=search) | Q(Product_Type__icontains=search)
            )

            if match:
                return render(request,'CRUD_Inventory/Admin_CRUD_Products.html',{'sr':match})

            else:
                messages.error(request,'No Result Found')

        else:
            return HttpResponseRedirect('/store/admin_products/')

    return render(request, 'CRUD_Inventory/Admin_CRUD_Products.html')

def upload_list(request):
    list_upload = upload_files.objects.all()
    return render(request,'CRUD_Inventory/uploaded.html',{'lists':list_upload})

    

def upload_file(request):
    if request.method == 'POST':
        form = request.POST 
        uploaded_file = request.FILES['document']
        file_namee = request.POST['file']
        file_type = request.POST['format']
        upload_files.objects.create(File_Name = file_namee,File_Type =file_type, pdf=uploaded_file)
        
        
    return render(request,'CRUD_Inventory/upload_file.html')

def run(request,id):
    a = upload_files.objects.get(id=id)
    a.delete()
    return HttpResponseRedirect('/store/admin_products/uploaded_file/')

# def uploaded_file(request):
#     return render(request,)
   


