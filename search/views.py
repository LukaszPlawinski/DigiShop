from django.shortcuts import render
from shop.models import Product, Category


# Create your views here.

def search (request):
    category = None
    categories = Category.objects.all()
    keyword = request.GET['q']
    products = Product.objects.filter(name__icontains=request.GET['q'])
    return render(request, "list.html", {"products": products, 'categories': categories, 'keyword':keyword})
