from django.shortcuts import render


# Create your views here.
def user_profile(request):
    context = {"title": "Profile",}
    return render(request, "user_profile/index.html", context)
