from django.shortcuts import render,HttpResponseRedirect,reverse
from store.models import *
from django.http import *
from django.db.models import Q
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import permission_required

#render all product and list them in store page 
def store(request):
    get_spec = Product.objects.all()[0:8] #get all product from database
    return render(request,'store.html',{'prod':get_spec})

@permission_required('store.add_product', login_url='restricted/')# django decorater to restricted pages
def admin_page(request):#render all product and list them in admin page
    obj=Product.objects.all()[0:8] 
    return render(request,'CRUD_Inventory/Admin_CRUD_Products.html',{'product':obj})

def admin_restricted(request):# render to restrcited page 
    return render(request,'CRUD_Inventory/restricted.html')

def upload(request):# render to upload page
    return render(request,'CRUD_Inventory/upload.html')
    
def uploaded_save(request):# saves product which are uploaded in database
    if request.method == 'POST':# to check for use of the POST method
        getall=request.POST 
        name=request.POST['Product_Name'] # create a form instance and populate it with data from the request
        typ=request.POST['Product_Type']
        price=request.POST['Product_Price']
        qty=request.POST['Product_Quantity']
        imagee = request.FILES['Product_Image']
        # create database and store in column
        Product.objects.create(Product_Name=name, Product_Type=typ,Product_Price=price,Product_Quantity=qty, img=imagee )
    return HttpResponseRedirect('/store/admin_products/')

def get_product(request,id):# Update form page for selected product
    get_id = Product.objects.get(id=id) # get the ID of selected product
    return render(request,'CRUD_Inventory/update.html',{'product':get_id})


# saves updated form of selected product
def update_product(request,id):
    get_id = Product.objects.get(id=id)
    get_request = request.POST
    get_id.Product_Name = request.POST['name']
    get_id.Product_Type = request.POST['type']
    get_id.Product_Price = request.POST['price']
    get_id.Product_Quantity = request.POST['qty']
    get_id.save()
    return HttpResponseRedirect('/store/admin_products/')

# delete selected product
def delete_product(request,id):
    x = Product.objects.get(id = id)
    x.delete()
    return HttpResponseRedirect('/store/admin_products/')
   
# search the product which are in manage prodct page   
def search(request):
    if request.method == 'GET':# to check for use of the Get method
        searc = request.GET['search']
        search=searc.strip()

        if search:
            match = Product.objects.filter(
                Q( Product_Name__icontains=search) | Q(Product_Type__icontains=search)
            ) #Filter the products which the user want to search from product list

            if match:
                return render(request,'CRUD_Inventory/Admin_CRUD_Products.html',{'sr':match})

            else:
                messages.error(request,'No Result Found') # shows message to user if there is no product which he want to search

        else:
            return HttpResponseRedirect('/store/admin_products/')

    return render(request, 'CRUD_Inventory/Admin_CRUD_Products.html')

#search in store page
def store_search(request):
    if request.method == 'GET':
        searc = request.GET['search']
        search=searc.strip()
        if search:
            match = Product.objects.filter(
                Q( Product_Name__icontains=search) | Q(Product_Type__icontains=search)
            )

            if match:
                return render(request,'store.html',{'search':match})

            else:
                messages.error(request,'No Result Found')

        else:
            return HttpResponseRedirect('/store/')

    return render(request, 'store.html')

##render page and view uploaded file
def upload_list(request):
    list_upload = upload_files.objects.all()
    return render(request,'CRUD_Inventory/uploaded.html',{'lists':list_upload})

    
#upload file 
def upload_file(request):
    if request.method == 'POST':
        form = request.POST 
        uploaded_file = request.FILES['document']
        file_namee = request.POST['file']
        file_type = request.POST['format']
        upload_files.objects.create(File_Name = file_namee,File_Type =file_type, pdf=uploaded_file)
        
        
    return render(request,'CRUD_Inventory/upload_file.html')

# delete selected file
def delete(request,id):
    a = upload_files.objects.get(id=id)
    a.delete()
    return HttpResponseRedirect('/store/admin_products/uploaded_file/')


 
# pagination for store page
def pagination(request,pageNo):
    get_prod=Product.objects.all()
    get_prod_slice=None
    
    if request.method == "GET":
         # range of 8, calculate where to slice the list
        strt_slice=(pageNo-1) * 8
        end_slice=(pageNo-1) * 8
        max_len=pageNo * 8
        data_avilbl=get_prod.count() #count all the products

        while end_slice < data_avilbl and end_slice < max_len:
            get_prod_slice=get_prod[strt_slice:end_slice+1]
            end_slice=end_slice+1
    
        return render(request,'store.html',{'v_img':get_prod_slice})

#pagination for admin page
def paginationForCRUD(request,pageNo):
    get_prod=Product.objects.all()
    get_prod_slice=None
    
    if request.method == "GET":
        strt_slice=(pageNo-1) * 8
        end_slice=(pageNo-1) * 8
        max_len=pageNo * 8
        data_avilbl=get_prod.count()  

        while end_slice < data_avilbl and end_slice < max_len:
            get_prod_slice=get_prod[strt_slice:end_slice+1]
            end_slice=end_slice+1
    
        return render(request,'CRUD_Inventory/Admin_CRUD_Products.html',{'prod':get_prod_slice})
