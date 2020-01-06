from django.shortcuts import render


# Create your views here.
def store(request):
    return render(request,'store.html')

def admin_page(request):
    return render(request,'Admin_CRUD_Products.html')
    