from django.shortcuts import render
from store.models import product

# Create your views here.
def store(request):
    return render(request,'store.html')

def admin_page(request):
    obj=product.objects.all()  
    return render(request,'Admin_CRUD_Products.html',{'product':obj})
    