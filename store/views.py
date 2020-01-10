from django.shortcuts import render
from store.models import *
from django.http import *
from django.db.models import Q
from django.contrib import messages
from django.core.files.storage import FileSystemStorage

# Create your views here.


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
   


