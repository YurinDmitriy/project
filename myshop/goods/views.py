from django.shortcuts import render
from .models import Categories, Products


# Create your views here.
def catalog(request):

    products = Products.objects.all()
    categories = Categories.objects.all()

    context = {
        "title": "Catalog",
        "products": products,
        "categories": categories,
    }
    return render(request, "goods/catalog.html", context)


def product(request, product_id):
    product = Products.objects.get(id=product_id)
    context = {
        "title": "Product",
        "product": product,
    }
    return render(request, "goods/product.html", context)
