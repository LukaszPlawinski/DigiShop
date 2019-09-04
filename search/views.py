from django.shortcuts import render
from shop.models import Product


# Create your views here.

def search (request):
    products = Product.objects.filter(name__icontains=request.GET['q'])
    return render(request, "list.html", {"products": products})
