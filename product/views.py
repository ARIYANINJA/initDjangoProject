from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_page(request ,*args, **kwargs):
    return render(request , 'index.html', {})   
    # return HttpResponse('<h1>hello world</h1>')
