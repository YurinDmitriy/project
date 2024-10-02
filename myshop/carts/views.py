from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from goods.models import Products
from .models import Cart
from .forms import CartChangeForm


# Create your views here.
def cart_add(request, product_slug):
    product = Products.objects.get(slug=product_slug)
    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, product=product)
        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(user=request.user, product=product, quantity=1)
    return redirect(request.META["HTTP_REFERER"])


def cart_change(request, product):

    form = CartChangeForm(
        data={
            "user": request.user,
            "product": product,
            "quantity": request.POST["quantity"],
        }
    )

    form.save()
    return HttpResponseRedirect(reverse("users:users_cart"))


def cart_remove(request, cart_id):
    cart = Cart.objects.get(id=cart_id)
    cart.delete()
    return redirect(request.META["HTTP_REFERER"])
