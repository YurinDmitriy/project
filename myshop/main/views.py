from django.shortcuts import render


# Create your views here.
def main(request):
    context = {
        "title": "Главная",
    }
    return render(request, "main/index.html", context)
