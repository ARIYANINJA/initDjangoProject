from django.shortcuts import render
from .models import Product, GeeksModel
from .forms import ProductForm
from django.views.generic.list import ListView


# Create your views here.
def home_page(request, *args, **kwargs):
    info = {"name": "ariya", "age": 22, "phone": 98189848, "list": [1, 2, 3, 4, 5, 6]}
    return render(request, "index.html", info)
    # return HttpResponse('<h1>hello world</h1>')


def productCreate(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    info = {"form": form}

    return render(request, "product_create.html", info)


def productDetail(request):
    obj = Product.objects.get(id=1)
    info = {"object": obj}
    return render(request, "product_detail.html", info)


class GeeksList(ListView):
    # specify the model for list view
    model = GeeksModel
