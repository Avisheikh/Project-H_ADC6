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
