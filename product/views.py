from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
# Create your views here.
def home_page(request ,*args, **kwargs):
    info = {
        'name' : 'ariya',
        'age' : 22,
        'phone' : 98189848,
        'list' : [1,2,3,4,5,6]
    }
    return render(request , 'index.html', info)   
    # return HttpResponse('<h1>hello world</h1>')

def productDetail(request):
    obj = Product.objects.get(id = 1)
    info = {
        'object' : obj
    }
    return render(request, 'product_detail.html', info )