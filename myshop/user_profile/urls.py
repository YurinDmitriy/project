from django.urls import path
from .views import *

app_name = "user_profile"
urlpatterns = [
    path("", user_profile, name="user_profile"),
]
