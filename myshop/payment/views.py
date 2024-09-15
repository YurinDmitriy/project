from django.shortcuts import render


# Create your views here.
def payment(request):
    context = {"title": "Payment",}
    return render(request, "payment/index.html", context)
